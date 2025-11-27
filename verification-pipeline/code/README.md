# Source Verification Pipeline

A three-stage pipeline for catching LLM confabulation when extracting claims from documents.

## The Problem

When LLMs extract information from documents, they confabulate: strip qualifiers, add framing, omit context. The pipeline makes these failure modes visible.

## Three Stages

| Stage | Actor | Purpose |
|-------|-------|---------|
| **1. Extraction** | LLM (Claude) | Extract claims with exact quotes + locations |
| **2. Verification** | Python script | Check quotes actually exist in source |
| **3. Adversarial** | LLM (Claude) | Attack claim-quote links, find context stripping |

## Files

```
code/
  verify-quotes.py      # Stage 2: Quote verification script
  prompts/
    extraction.md       # Stage 1: Extraction prompt template
    adversarial.md      # Stage 3: Adversarial review prompt template
  skills/
    extract-claims.md   # Claude Code skill for extraction
    find-source.md      # Claude Code skill for source location
  agents/
    chunk-processor.md  # Claude Code subagent for batch processing
```

## Usage

### Stage 1: Extraction

Use the extraction prompt with any LLM, or invoke the `extract-claims` skill in Claude Code.

**Input:** Source document(s)
**Output:** JSON file with claims and quotes

```json
{
  "claims": [
    {
      "claim": "Your interpretation",
      "quote": "EXACT text - copy precisely",
      "source": "filename.md",
      "line": 42
    }
  ]
}
```

### Stage 2: Verification

```bash
python3 verify-quotes.py claims.json source_dir/
```

**Handles:**
- PDF extraction artifacts (word-per-line formatting)
- Ligatures (fi, fl, ff, ffi, ffl)
- Smart quotes and dashes
- Fuzzy matching with similarity scores

**Output:**
- Console summary
- `claims.verified.json` with detailed results

**Thresholds:**
- 100% match (after normalization) → VERIFIED
- \>85% match → REVIEW NEEDED
- \>60% match → POSSIBLE MATCH
- <60% → FAILED

### Stage 3: Adversarial Review

Use the adversarial prompt with any LLM.

**For each claim, it asks:**
1. Does the quote actually support the claim?
2. Is important context being stripped?
3. Could the quote support a DIFFERENT interpretation?
4. Is causal significance being inflated?

**Verdicts:**
- **SOLID** — Direct quote match, no interpretation added
- **WEAKENED** — Stripped qualifiers, added framing, interpretive layering
- **REFUTED** — Omitted exculpatory context that changes meaning

## Common Confabulation Patterns

From testing on Anthropic's Claude Opus 4.5 System Card:

| Pattern | Example |
|---------|---------|
| Context omission | "We don't find this concerning" stripped |
| Interpretive layering | "suggest" → presented as fact |
| Intentionality framing | Neutral description → "the model omitted" |
| Correlation → causation | "corroborated hypothesis" → established cause |
| Qualifier stripping | "most likely" → "believed to be" |

## Claude Code Integration

The `skills/` and `agents/` directories contain Claude Code configuration for running this pipeline:

- **extract-claims** skill: Extract verifiable claims from any article
- **find-source** skill: Locate exact source for a claim
- **chunk-processor** agent: Process large documents chunk-by-chunk

To use, copy to your `.claude/skills/` or `.claude/agents/` directory.

## Example Output

See the verification artifacts in this repository:
- [06b-claims.json](../06b-claims.json) — Extracted claims
- [06b-adversarial.md](../06b-adversarial.md) — Adversarial review results

---

## License

MIT License. See [LICENSE](LICENSE).

## Disclaimer

This pipeline is an experimental tool for making LLM confabulation patterns *visible*. It does not guarantee accuracy, prevent errors, or catch all forms of misrepresentation.

**This software is provided "as is" without warranty of any kind.** The authors are not liable for any damages or consequences arising from its use. You are responsible for verifying any outputs and ensuring they meet your requirements.

The pipeline helps—it doesn't solve. Use it as one tool among many, not as a source of truth.

---

*Built with Claude Opus 4.5*
