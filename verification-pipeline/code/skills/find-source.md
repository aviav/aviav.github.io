---
name: find-source
description: Find source location (file and line number) for a claim in a corpus of documents. Use when verifying extracted claims against original sources.
allowed-tools: Read, Grep, Glob
---

# Find Source

## Purpose

Given a claim and a source corpus, locate the exact file and line number where the claim originates.

## Process

1. Receive claim to verify
2. Identify key terms/phrases to search
3. Grep across source corpus
4. Read matching files to confirm context
5. Return file:line_number or "NOT FOUND"

## Output Format

```markdown
## Claim: [the claim]

**Status:** VERIFIED | PARTIALLY VERIFIED | NOT FOUND | INACCURATE

**Source:** `path/to/file.md:123`

**Original text:**
> [exact quote from source]

**Notes:** [any discrepancies or context]
```

## Verification levels

- **VERIFIED**: Exact match or faithful paraphrase found
- **PARTIALLY VERIFIED**: Claim is based on source but simplified/interpreted
- **NOT FOUND**: Cannot locate source for this claim
- **INACCURATE**: Source says something different than claimed

## Search strategy

1. Start with distinctive phrases (quoted text, technical terms)
2. Fall back to key concept words
3. Check multiple files if claim could appear in several places
4. Note if claim synthesizes across multiple sources
