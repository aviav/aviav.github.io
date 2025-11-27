# Stage 1: Claim Extraction Prompt

Use this prompt with any LLM to extract verifiable claims from a document.

---

## Prompt

```
You are extracting verifiable claims from [source]. Your job is to produce EXACT quotes.

Read: [source file]

Extract N key claims. For EACH claim:
1. State the claim in your own words
2. Provide the EXACT quote from the source (copy-paste precisely)
3. Note the source filename
4. Estimate the line number

Output as JSON to: [output path]

Format:
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

CRITICAL: Quotes must be EXACT. A verification script will check character-by-character.
```

---

## Usage Notes

- Replace `[source]` with document name/description
- Replace `[source file]` with actual file path
- Replace `N` with desired number of claims (or "all key")
- Replace `[output path]` with where to save JSON

## What Makes Good Claims

**Extract:**
- Statistics and numbers
- Direct quotes from sources
- Technical claims about how things work
- Claims about what documents say
- Behavioral or capability claims

**Skip:**
- Author's opinions and reflections
- Rhetorical questions
- Hedged speculation explicitly marked as uncertain
- Meta-commentary about the writing itself
