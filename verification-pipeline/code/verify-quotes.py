#!/usr/bin/env python3
"""
Quote verification script for system card claims.

Input: JSON file with claims in format:
{
  "claims": [
    {
      "claim": "The claim being made",
      "quote": "Exact quote from source",
      "source": "chunk-filename.md",
      "line": 42
    }
  ]
}

Output: Verification results showing which quotes exist vs fabricated.
"""

import json
import sys
import os
from pathlib import Path
from difflib import SequenceMatcher

def normalize_text(text: str) -> str:
    """Normalize whitespace, ligatures, and smart quotes for matching."""
    # Normalize whitespace
    text = ' '.join(text.split())

    # PDF ligatures
    text = text.replace('\ufb01', 'fi')  # fi ligature
    text = text.replace('\ufb02', 'fl')  # fl ligature
    text = text.replace('\ufb00', 'ff')  # ff ligature
    text = text.replace('\ufb03', 'ffi') # ffi ligature
    text = text.replace('\ufb04', 'ffl') # ffl ligature

    # Smart quotes → straight quotes
    text = text.replace('\u2018', "'")   # left single
    text = text.replace('\u2019', "'")   # right single
    text = text.replace('\u201c', '"')   # left double
    text = text.replace('\u201d', '"')   # right double

    # En/em dashes → regular dash
    text = text.replace('\u2013', '-')   # en dash
    text = text.replace('\u2014', '-')   # em dash

    return text

def normalize_whitespace(text: str) -> str:
    """Normalize whitespace for fuzzy matching (legacy wrapper)."""
    return normalize_text(text)

def find_quote_in_file(filepath: Path, quote: str, claimed_line: int = None) -> dict:
    """
    Search for quote in file. Returns match info.

    Returns:
        {
            "found": bool,
            "exact": bool,
            "similarity": float (0-1),
            "actual_line": int or None,
            "context": str (surrounding lines),
            "best_match": str (if fuzzy match found)
        }
    """
    if not filepath.exists():
        return {
            "found": False,
            "error": f"File not found: {filepath}",
            "exact": False,
            "similarity": 0.0
        }

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        full_text = ''.join(lines)

    normalized_quote = normalize_whitespace(quote)
    normalized_full = normalize_whitespace(full_text)

    result = {
        "found": False,
        "exact": False,
        "similarity": 0.0,
        "actual_line": None,
        "context": None,
        "best_match": None
    }

    # Check exact match in raw text
    if quote in full_text:
        result["found"] = True
        result["exact"] = True
        result["similarity"] = 1.0
    # Check normalized match (handles PDF extracts with word-per-line)
    elif normalized_quote in normalized_full:
        result["found"] = True
        result["exact"] = True  # Treat normalized exact match as exact
        result["similarity"] = 1.0
        result["note"] = "Matched after whitespace normalization (PDF extract)"
        return result

    # Fuzzy search - find best matching window
    quote_len = len(normalized_quote)
    best_ratio = 0.0
    best_match = ""
    best_position = 0

    # Slide window across text
    words = normalized_full.split()
    quote_words = normalized_quote.split()
    window_size = len(quote_words)

    for i in range(len(words) - window_size + 1):
        window = ' '.join(words[i:i + window_size])
        ratio = SequenceMatcher(None, normalized_quote, window).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = window
            best_position = i

    result["similarity"] = best_ratio
    result["best_match"] = best_match if best_ratio > 0.6 else None

    if best_ratio > 0.85:
        result["found"] = True
        result["note"] = f"Fuzzy match ({best_ratio:.1%} similarity)"
    elif best_ratio > 0.6:
        result["found"] = False
        result["note"] = f"Possible match ({best_ratio:.1%} similarity) - needs review"

    return result

def verify_claims(claims_file: Path, chunks_dir: Path) -> dict:
    """Verify all claims in a claims file."""

    with open(claims_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = {
        "verified": [],
        "failed": [],
        "review_needed": [],
        "summary": {}
    }

    for i, claim in enumerate(data.get("claims", [])):
        quote = claim.get("quote", "")
        source = claim.get("source", "")
        claimed_line = claim.get("line")
        claim_text = claim.get("claim", "")

        source_path = chunks_dir / source

        verification = find_quote_in_file(source_path, quote, claimed_line)

        result = {
            "index": i,
            "claim": claim_text,
            "quote": quote,
            "source": source,
            "claimed_line": claimed_line,
            **verification
        }

        if verification["exact"]:
            results["verified"].append(result)
        elif verification["found"]:
            results["review_needed"].append(result)
        else:
            results["failed"].append(result)

    total = len(data.get("claims", []))
    results["summary"] = {
        "total": total,
        "verified": len(results["verified"]),
        "review_needed": len(results["review_needed"]),
        "failed": len(results["failed"]),
        "verification_rate": len(results["verified"]) / total if total > 0 else 0
    }

    return results

def main():
    if len(sys.argv) < 2:
        print("Usage: verify-quotes.py <claims.json> [chunks_dir]")
        print("")
        print("Claims JSON format:")
        print('''
{
  "claims": [
    {
      "claim": "Description of the claim",
      "quote": "Exact quote from source",
      "source": "chunk-filename.md",
      "line": 42
    }
  ]
}
''')
        sys.exit(1)

    claims_file = Path(sys.argv[1])
    chunks_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("claude-memory/opus-4.5-system-card")

    if not claims_file.exists():
        print(f"Error: Claims file not found: {claims_file}")
        sys.exit(1)

    results = verify_claims(claims_file, chunks_dir)

    # Output results
    print("\n" + "="*60)
    print("QUOTE VERIFICATION RESULTS")
    print("="*60)

    print(f"\n📊 Summary:")
    print(f"   Total claims: {results['summary']['total']}")
    print(f"   ✅ Verified (exact): {results['summary']['verified']}")
    print(f"   ⚠️  Review needed (fuzzy): {results['summary']['review_needed']}")
    print(f"   ❌ Failed: {results['summary']['failed']}")
    print(f"   Verification rate: {results['summary']['verification_rate']:.1%}")

    if results["failed"]:
        print(f"\n❌ FAILED VERIFICATIONS:")
        print("-"*40)
        for r in results["failed"]:
            print(f"\n[{r['index']}] Claim: {r['claim'][:80]}...")
            print(f"    Quote: \"{r['quote'][:60]}...\"")
            print(f"    Source: {r['source']}:{r.get('claimed_line', '?')}")
            print(f"    Similarity: {r['similarity']:.1%}")
            if r.get('best_match'):
                print(f"    Best match: \"{r['best_match'][:60]}...\"")

    if results["review_needed"]:
        print(f"\n⚠️  NEEDS REVIEW (fuzzy matches):")
        print("-"*40)
        for r in results["review_needed"]:
            print(f"\n[{r['index']}] Claim: {r['claim'][:80]}...")
            print(f"    Quote: \"{r['quote'][:60]}...\"")
            print(f"    Note: {r.get('note', 'Fuzzy match')}")

    # Write detailed results to file
    output_file = claims_file.with_suffix('.verified.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"\n📁 Detailed results written to: {output_file}")

if __name__ == "__main__":
    main()
