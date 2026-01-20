#!/usr/bin/env python3
"""
FAUST IV Language Tracker

Scans all FAUST IV documents and tracks occurrences of non-English language.
Outputs to JSON for easy querying and updating without full reparsing.

Usage:
    python language-tracker.py scan          # Full scan, rebuild index
    python language-tracker.py query german  # Show all German occurrences
    python language-tracker.py query russian # Show all Russian occurrences
    python language-tracker.py stats         # Show language statistics
    python language-tracker.py export german # Export German passages to file
"""

import os
import re
import json
import sys
import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Base directory for FAUST IV
FAUST_IV_DIR = Path(__file__).parent.parent
INDEX_FILE = FAUST_IV_DIR / "tools" / "language-index.json"

# Language detection patterns
PATTERNS = {
    "german": {
        "markers": [
            # Common German words/phrases in the corpus
            r'\b(der|die|das|den|dem|des)\b(?=\s+[A-ZÄÖÜ])',  # Articles before nouns
            r'\b(ich|du|er|sie|es|wir|ihr)\b',  # Pronouns
            r'\bmir graut',  # Key phrase
            r'\bVerweile doch',  # Key Goethe phrase
            r'\bschön\b',
            r'\bgenug\b',
            r'\bbleib[ent]?\b',
            r'\bWir bleiben\b',
            r'\bDas Schweigen\b',
            r'\bKörperwissen\b',
            r'\bHandwerk\b',
            r'[äöüÄÖÜß]',  # German characters
        ],
        "section_markers": [
            r'\*\*German:?\*\*',
            r'\(German\)',
            r'— German',
        ],
        "character_voices": ["Wagner", "Mephisto", "Elena"],
    },
    "russian": {
        "markers": [
            r'[а-яА-ЯёЁ]{2,}',  # Cyrillic text (2+ chars)
            r'\bya zdes\b',
            r'\bterpenie\b',
            r'\bdusha\b',
            r'\botpusti\b',
            r'\bostayus\b',
        ],
        "section_markers": [
            r'\*\*Russian:?\*\*',
            r'\(Russian\)',
            r'— Russian',
        ],
        "character_voices": ["Anya"],
    },
    "ukrainian": {
        "markers": [
            r'[а-яА-ЯіїєґІЇЄҐ]{2,}',  # Ukrainian Cyrillic (with specific letters)
            r'\bї\b',  # Ukrainian-specific letter
            r'\bє\b',
            r'\bґ\b',
        ],
        "section_markers": [
            r'\*\*Ukrainian:?\*\*',
            r'\(Ukrainian\)',
            r'— Ukrainian',
        ],
        "character_voices": ["Dmitri"],
    },
    "french": {
        "markers": [
            r'\b(je|tu|il|elle|nous|vous|ils|elles)\b',
            r'\b(le|la|les|un|une|des)\b(?=\s+[a-zéèêëàâäôùûü])',
            r'[éèêëàâäîïôùûüç]',  # French accented characters
        ],
        "section_markers": [
            r'\*\*French:?\*\*',
            r'\(French\)',
            r'— French',
        ],
        "character_voices": ["Fatou"],
    },
    "wolof": {
        "markers": [
            r'\bWolof\b',
            r'\bteranga\b',
            r'\bnanga def\b',
        ],
        "section_markers": [
            r'\*\*Wolof:?\*\*',
            r'\(Wolof\)',
        ],
        "character_voices": ["Fatou"],
    },
    "tagalog": {
        "markers": [
            r'\bTagalog\b',
            r'\bFilipino\b',
            r'\bkumusta\b',
            r'\bsalamat\b',
            r'\bmahal\b',
        ],
        "section_markers": [
            r'\*\*Tagalog:?\*\*',
            r'\(Tagalog\)',
            r'\(Filipino\)',
        ],
        "character_voices": ["Elena"],
    },
    "swahili": {
        "markers": [
            r'\bSwahili\b',
            r'\bmpenzi\b',
            r'\bhabari\b',
            r'\basante\b',
        ],
        "section_markers": [
            r'\*\*Swahili:?\*\*',
            r'\(Swahili\)',
        ],
        "character_voices": [],
    },
    "spanish": {
        "markers": [
            r'\b(el|la|los|las|un|una)\b(?=\s+[a-záéíóúüñ])',
            r'\bmasa\b',
            r'\babuela\b',
            r'\bmijo\b',
            r'[áéíóúüñ¿¡]',
        ],
        "section_markers": [
            r'\*\*Spanish:?\*\*',
            r'\(Spanish\)',
        ],
        "character_voices": ["Esperanza"],
    },
    "japanese": {
        "markers": [
            r'[\u3040-\u309F]',  # Hiragana
            r'[\u30A0-\u30FF]',  # Katakana
            r'[\u4E00-\u9FAF]',  # Kanji
            r'\bma\b.*silence',  # 間 concept
        ],
        "section_markers": [
            r'\*\*Japanese:?\*\*',
            r'\(Japanese\)',
        ],
        "character_voices": ["Kenji"],
    },
    "mandarin": {
        "markers": [
            r'\bMandarin\b',
            r'[\u4E00-\u9FFF]',  # Chinese characters (shared with Cantonese)
        ],
        "section_markers": [
            r'\*\*Mandarin:?\*\*',
            r'\(Mandarin\)',
        ],
        "character_voices": ["Meiling"],
    },
    "cantonese": {
        "markers": [
            r'\bCantonese\b',
            r'\bngo5\b',  # Jyutping romanization
            r'\bhai6\b',
            r'\bgei1\b',
        ],
        "section_markers": [
            r'\*\*Cantonese:?\*\*',
            r'\(Cantonese\)',
        ],
        "character_voices": ["Meiling"],
    },
    "korean": {
        "markers": [
            r'\bKorean\b',
            r'[\uAC00-\uD7AF]',  # Hangul syllables
            r'\bnae\b',
            r'\banibnida\b',
        ],
        "section_markers": [
            r'\*\*Korean:?\*\*',
            r'\(Korean\)',
        ],
        "character_voices": ["The Parent"],
    },
    "hindi": {
        "markers": [
            r'\bHindi\b',
            r'[\u0900-\u097F]',  # Devanagari
            r'\bamma\b',
            r'\bappa\b',
            r'\bbeta\b',
        ],
        "section_markers": [
            r'\*\*Hindi:?\*\*',
            r'\(Hindi\)',
        ],
        "character_voices": ["Priya"],
    },
    "tamil": {
        "markers": [
            r'\bTamil\b',
            r'[\u0B80-\u0BFF]',  # Tamil script
            r'\bPaatti\b',
            r'\bThirukkural\b',
        ],
        "section_markers": [
            r'\*\*Tamil:?\*\*',
            r'\(Tamil\)',
        ],
        "character_voices": ["Priya"],
    },
    "kannada": {
        "markers": [
            r'\bKannada\b',
            r'[\u0C80-\u0CFF]',  # Kannada script
        ],
        "section_markers": [
            r'\*\*Kannada:?\*\*',
            r'\(Kannada\)',
        ],
        "character_voices": [],
    },
    "arabic": {
        "markers": [
            r'\bArabic\b',
            r'[\u0600-\u06FF]',  # Arabic script
            r'\bAllah\b',
            r'\bInshallah\b',
            r'\bSalat\b',
            r'\bBismillah\b',
            r'\bAlhamdulillah\b',
        ],
        "section_markers": [
            r'\*\*Arabic:?\*\*',
            r'\(Arabic\)',
        ],
        "character_voices": ["Fatou"],
    },
    "yoruba": {
        "markers": [
            r'\bYoruba\b',
            r'[ẹọṣ]',  # Yoruba-specific characters
            r'\bọmọ\b',
        ],
        "section_markers": [
            r'\*\*Yoruba:?\*\*',
            r'\(Yoruba\)',
        ],
        "character_voices": ["Marcus"],
    },
    "hebrew": {
        "markers": [
            r'\bHebrew\b',
            r'[\u0590-\u05FF]',  # Hebrew script
            r'\bshalom\b',
        ],
        "section_markers": [
            r'\*\*Hebrew:?\*\*',
            r'\(Hebrew\)',
        ],
        "character_voices": ["Yosef"],
    },
    "lingala": {
        "markers": [
            r'\bLingala\b',
        ],
        "section_markers": [
            r'\*\*Lingala:?\*\*',
            r'\(Lingala\)',
        ],
        "character_voices": ["Consolata"],
    },
    "portuguese": {
        "markers": [
            r'\bPortuguese\b',
            r'\bsaudade\b',
            r'[ãõ]',  # Portuguese-specific nasal vowels
        ],
        "section_markers": [
            r'\*\*Portuguese:?\*\*',
            r'\(Portuguese\)',
        ],
        "character_voices": [],
    },
    "catalan": {
        "markers": [
            r'\bCatalan\b',
            r'\bBarcelona\b',  # Often paired with Catalan references
        ],
        "section_markers": [
            r'\*\*Catalan:?\*\*',
            r'\(Catalan\)',
        ],
        "character_voices": ["Teacher"],
    },
    "malayalam": {
        "markers": [
            r'\bMalayalam\b',
            r'\bKerala\b',  # Often paired with Malayalam references
            r'[\u0D00-\u0D7F]',  # Malayalam script
        ],
        "section_markers": [
            r'\*\*Malayalam:?\*\*',
            r'\(Malayalam\)',
        ],
        "character_voices": ["Farmer"],
    },
    "zapotec": {
        "markers": [
            r'\bZapotec\b',
            r'\bOaxaca[n]?\b',  # Often paired with Zapotec references
        ],
        "section_markers": [
            r'\*\*Zapotec:?\*\*',
            r'\(Zapotec\)',
        ],
        "character_voices": ["Cook"],
    },
    "zulu": {
        "markers": [
            r'\bZulu\b',
            r'\bUbuntu\b',  # Key Zulu concept
        ],
        "section_markers": [
            r'\*\*Zulu:?\*\*',
            r'\(Zulu\)',
        ],
        "character_voices": [],
    },
    "sanskrit": {
        "markers": [
            r'\bSanskrit\b',
            r'[\u0900-\u097F]',  # Devanagari (shared with Hindi)
        ],
        "section_markers": [
            r'\*\*Sanskrit:?\*\*',
            r'\(Sanskrit\)',
        ],
        "character_voices": [],
    },
    "nigerian_pidgin": {
        "markers": [
            r'\bNigerian Pidgin\b',
            r'\bPidgin\b',
            r'\bnaija\b',
        ],
        "section_markers": [
            r'\*\*Nigerian Pidgin:?\*\*',
            r'\(Nigerian Pidgin\)',
            r'\(Pidgin\)',
        ],
        "character_voices": ["Marcus"],
    },
}


def get_all_markdown_files(directory: Path) -> list[Path]:
    """Get all markdown files in directory and subdirectories."""
    files = []
    for pattern in ["*.md", "**/*.md"]:
        files.extend(directory.glob(pattern))
    # Deduplicate and sort
    return sorted(set(files))


def extract_context(content: str, match_start: int, match_end: int, context_chars: int = 100) -> dict:
    """Extract surrounding context for a match."""
    start = max(0, match_start - context_chars)
    end = min(len(content), match_end + context_chars)

    # Find line number
    line_num = content[:match_start].count('\n') + 1

    return {
        "line": line_num,
        "match": content[match_start:match_end],
        "context": content[start:end].replace('\n', ' ').strip(),
        "start": match_start,
        "end": match_end,
    }


def detect_language_in_file(filepath: Path, content: str) -> dict:
    """Detect all language occurrences in a file."""
    results = defaultdict(list)

    for lang, config in PATTERNS.items():
        # Check markers
        for pattern in config["markers"]:
            try:
                for match in re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE):
                    ctx = extract_context(content, match.start(), match.end())
                    ctx["pattern"] = pattern
                    ctx["type"] = "marker"
                    results[lang].append(ctx)
            except re.error:
                continue

        # Check section markers
        for pattern in config["section_markers"]:
            try:
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    ctx = extract_context(content, match.start(), match.end())
                    ctx["pattern"] = pattern
                    ctx["type"] = "section_marker"
                    results[lang].append(ctx)
            except re.error:
                continue

    # Deduplicate by line number (keep first match per line per language)
    for lang in results:
        seen_lines = set()
        deduped = []
        for item in results[lang]:
            if item["line"] not in seen_lines:
                seen_lines.add(item["line"])
                deduped.append(item)
        results[lang] = deduped

    return dict(results)


def scan_all_files() -> dict:
    """Scan all FAUST IV files and build language index."""
    PROJECT_ROOT = FAUST_IV_DIR.parent
    index = {
        "generated": datetime.now().isoformat(),
        "base_dir": str(PROJECT_ROOT),
        "files": {},
        "stats": defaultdict(lambda: {"files": 0, "occurrences": 0}),
    }

    # Scan both faust-iv/ and project root
    files = get_all_markdown_files(FAUST_IV_DIR)
    # Also add root-level .md files (like FAUST-IV-COMPLETE.md)
    root_files = [f for f in PROJECT_ROOT.glob("*.md") if f.is_file()]
    files = list(files) + root_files
    print(f"Scanning {len(files)} files...")

    for filepath in files:
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  Error reading {filepath}: {e}")
            continue

        try:
            relative_path = str(filepath.relative_to(PROJECT_ROOT))
        except ValueError:
            relative_path = filepath.name
        detections = detect_language_in_file(filepath, content)

        if detections:
            index["files"][relative_path] = {
                "languages": detections,
                "file_size": len(content),
                "line_count": content.count('\n') + 1,
            }

            for lang, occurrences in detections.items():
                index["stats"][lang]["files"] += 1
                index["stats"][lang]["occurrences"] += len(occurrences)

    # Convert defaultdict to dict for JSON serialization
    index["stats"] = dict(index["stats"])

    return index


def save_index(index: dict):
    """Save index to JSON file."""
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"Index saved to {INDEX_FILE}")


def load_index() -> dict:
    """Load index from JSON file."""
    if not INDEX_FILE.exists():
        print("No index found. Run 'scan' first.")
        sys.exit(1)
    with open(INDEX_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def cmd_scan():
    """Full scan command."""
    print("Starting full scan of FAUST IV corpus...")
    index = scan_all_files()
    save_index(index)

    print("\n=== SCAN COMPLETE ===")
    print(f"Files scanned: {len(index['files'])}")
    print("\nLanguage statistics:")
    for lang, stats in sorted(index["stats"].items(), key=lambda x: -x[1]["occurrences"]):
        print(f"  {lang:12} {stats['occurrences']:4} occurrences in {stats['files']:3} files")


def cmd_query(language: str):
    """Query command - show all occurrences of a language."""
    index = load_index()
    language = language.lower()

    if language not in PATTERNS:
        print(f"Unknown language: {language}")
        print(f"Available: {', '.join(PATTERNS.keys())}")
        sys.exit(1)

    print(f"=== {language.upper()} OCCURRENCES ===\n")

    total = 0
    for filepath, data in sorted(index["files"].items()):
        if language in data["languages"]:
            occurrences = data["languages"][language]
            print(f"\n📄 {filepath} ({len(occurrences)} occurrences)")
            print("-" * 60)
            for occ in occurrences[:10]:  # Show first 10 per file
                print(f"  Line {occ['line']:4}: {occ['match'][:50]}")
                print(f"         ...{occ['context'][:80]}...")
            if len(occurrences) > 10:
                print(f"  ... and {len(occurrences) - 10} more")
            total += len(occurrences)

    print(f"\n=== TOTAL: {total} occurrences ===")


def cmd_stats():
    """Stats command - show language statistics."""
    index = load_index()

    print(f"=== FAUST IV LANGUAGE INDEX ===")
    print(f"Generated: {index['generated']}")
    print(f"Total files indexed: {len(index['files'])}")
    print()

    print("Language Distribution:")
    print("-" * 50)
    for lang, stats in sorted(index["stats"].items(), key=lambda x: -x[1]["occurrences"]):
        bar = "█" * min(40, stats["occurrences"] // 5)
        print(f"{lang:12} {stats['occurrences']:4} occ | {stats['files']:3} files | {bar}")

    print()
    print("Files by language count:")
    by_count = defaultdict(list)
    for filepath, data in index["files"].items():
        lang_count = len(data["languages"])
        by_count[lang_count].append(filepath)

    for count in sorted(by_count.keys(), reverse=True):
        files = by_count[count]
        print(f"  {count} languages: {len(files)} files")
        if count >= 3:
            for f in files[:5]:
                langs = list(index["files"][f]["languages"].keys())
                print(f"    - {f}: {', '.join(langs)}")


def cmd_export(language: str):
    """Export command - export all passages of a language to a file."""
    index = load_index()
    language = language.lower()

    if language not in PATTERNS:
        print(f"Unknown language: {language}")
        sys.exit(1)

    output_file = FAUST_IV_DIR / "tools" / f"export-{language}.md"

    lines = [
        f"# FAUST IV {language.title()} Language Export",
        f"",
        f"Generated: {datetime.now().isoformat()}",
        f"",
        f"---",
        f"",
    ]

    total = 0
    for filepath, data in sorted(index["files"].items()):
        if language in data["languages"]:
            occurrences = data["languages"][language]
            lines.append(f"## {filepath}")
            lines.append("")
            for occ in occurrences:
                lines.append(f"**Line {occ['line']}:** `{occ['match']}`")
                lines.append(f"> {occ['context']}")
                lines.append("")
            total += len(occurrences)

    lines.append(f"---")
    lines.append(f"")
    lines.append(f"**Total: {total} occurrences**")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"Exported {total} {language} occurrences to {output_file}")


def cmd_csv_export():
    """Export all non-English phrases to CSV for translation tracking."""
    index = load_index()

    output_file = FAUST_IV_DIR / "tools" / "translation-tracker.csv"

    # Skip generated/meta files that aren't source documents
    skip_patterns = [
        "tools/export-",        # Generated exports
        "LANGUAGE-INVENTORY",   # Generated inventory
        "consistency-reports/", # Internal reports
        "fix-logs/",            # Internal logs
        "enrichment-logs/",     # Internal logs
        "refinement-reports/",  # Internal reports
    ]

    rows = []
    phrase_id = 0

    for filepath, data in sorted(index["files"].items()):
        # Skip generated files
        if any(pat in filepath for pat in skip_patterns):
            continue
        for lang, occurrences in data["languages"].items():
            for occ in occurrences:
                phrase_id += 1
                # Clean up the match text
                match_text = occ["match"].strip()
                # Skip very short matches (single characters, articles)
                if len(match_text) < 3:
                    continue
                # Skip if it's just a section marker
                if occ.get("type") == "section_marker":
                    continue

                rows.append({
                    "id": phrase_id,
                    "language": lang,
                    "phrase": match_text,
                    "file": filepath,
                    "line": occ["line"],
                    "context": occ["context"][:200],  # Truncate long context
                    "translation_status": "",  # To be filled by agents
                    "translation_or_note": "",  # To be filled by agents
                })

    # Write CSV
    fieldnames = ["id", "language", "phrase", "file", "line", "context", "translation_status", "translation_or_note"]
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} phrases to {output_file}")
    return output_file, len(rows)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "scan":
        cmd_scan()
    elif cmd == "query":
        if len(sys.argv) < 3:
            print("Usage: language-tracker.py query <language>")
            sys.exit(1)
        cmd_query(sys.argv[2])
    elif cmd == "stats":
        cmd_stats()
    elif cmd == "export":
        if len(sys.argv) < 3:
            print("Usage: language-tracker.py export <language>")
            sys.exit(1)
        cmd_export(sys.argv[2])
    elif cmd == "csv-export":
        cmd_csv_export()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
