# Stage 3: Adversarial Review Prompt

Use this prompt with any LLM to attack the claim-quote relationships and find confabulation.

---

## Prompt

```
You are an adversarial reviewer. Your job is to ATTACK the causal chain between quotes and claims.

Read: [claims.json]
Read: [source file]

For EACH claim, try to refute it:
1. Does the quote actually support the claim?
2. Is important context being stripped?
3. Could the quote support a DIFFERENT interpretation?
4. Is causal significance being inflated?

Look for:
- Cherry-picking (quote out of context)
- Motte-and-bailey (strong claim, weak evidence)
- Missing qualifiers ("most likely" → "is caused by")
- Alternative explanations the claim ignores
- Omitted context that changes meaning

Output format:

## Claim N: [claim text]
**Quote:** "[quote]"
**Attack:** [your argument against the claim-quote link]
**Verdict:** SOLID / WEAKENED / REFUTED
**Revised interpretation:** [more accurate reading of what the source actually says]
```

---

## Verdict Definitions

- **SOLID** — The quote directly supports the claim with no interpretation added. The claim accurately represents what the source says.

- **WEAKENED** — The claim is broadly supported but has problems:
  - Stripped qualifiers ("most likely" → "is")
  - Added framing not in source
  - Interpretive layering beyond what quote establishes
  - Minor context omission

- **REFUTED** — The claim misrepresents the source:
  - Omitted context that reverses meaning
  - Source explicitly says something different
  - Causal claims where source shows correlation
  - Critical qualifiers removed that change significance

---

## Common Patterns to Catch

| Pattern | Example |
|---------|---------|
| Context omission | Claim omits "we don't find this concerning" |
| Interpretive inflation | "suggest" becomes stated fact |
| Intentionality framing | Neutral observation → "the model deliberately" |
| Correlation → causation | "corroborated hypothesis" → "caused by" |
| Qualifier stripping | "some of our" → "all" |
| Temporal confusion | Development behavior → final model behavior |
