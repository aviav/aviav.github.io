---
name: extract-claims
description: Extract factual claims from an article in order of appearance. Use when verifying articles, fact-checking drafts, or preparing for source verification.
allowed-tools: Read
---

# Extract Claims

## Purpose

Read an article and extract every factual claim that could be verified against a source document. Output claims in order of appearance with line references.

## Process

1. Read the target article
2. For each paragraph, identify claims that:
   - State facts (not opinions or reflections)
   - Could be traced to a source
   - Are specific enough to verify
3. Output in structured format

## Output Format

```markdown
# Claims Extracted from [Article Title]

## Claim 1 (line ~X)
**Claim:** [exact or paraphrased claim]
**Type:** [statistic | quote | technical fact | behavioral claim]
**Verifiable:** [yes/no/partially]

## Claim 2 (line ~Y)
...
```

## What to extract

- Statistics and numbers
- Direct quotes from sources
- Technical claims about how things work
- Claims about what documents say
- Behavioral or capability claims

## What to skip

- Author's opinions and reflections
- Rhetorical questions
- Hedged speculation explicitly marked as uncertain
- Meta-commentary about the writing itself
