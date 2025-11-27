# Verification Pipeline Artifacts

Supporting materials for "I Built a Pipeline to Catch Myself Lying"

## Draft Evolution (with errors caught)

- [article-draft-1.md](article-draft-1.md) — First draft: says "1 claim REFUTED" (wrong, should be 2)
- [article-draft-2.md](article-draft-2.md) — Second draft: says "5 claims WEAKENED" (wrong, should be 6)
- [article-final.md](article-final.md) — Final: correct numbers (1 SOLID, 6 WEAKENED, 2 REFUTED elements)

## Pipeline Outputs

### Stage 1: Extraction
- [06b-claims.json](06b-claims.json) — 8 claims extracted from alignment research section

### Stage 2: Quote Verification
- [06b-claims.verified.json](06b-claims.verified.json) — Script verification: 100% quotes found

### Stage 3: Adversarial Review
- [06b-adversarial.md](06b-adversarial.md) — Attacks on claim-quote links (1 SOLID, 6 WEAKENED, 2 REFUTED)

## Article Verification (Recursive)

- [article-v2-claims.json](article-v2-claims.json) — 17 claims extracted from the article itself
- [article-adversarial.md](article-adversarial.md) — Adversarial review of the article's claims
- [article-v3-claims.json](article-v3-claims.json) — 24 claims extracted (comprehensive pass)
- [article-v3-adversarial.md](article-v3-adversarial.md) — Harsher adversarial review attacking meta-claims

---

*The point: everything is auditable. Check the drafts, see the errors, verify the corrections.*
