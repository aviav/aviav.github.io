# System Card Claim Verification Report

**Article:** corpus-vs-system-card-article.md
**Source:** Opus 4.5 System Card (claude-memory/opus-4.5-system-card/)
**Date:** 2025-11-27
**Verifier:** Main agent (Opus 4.5)

---

## Claims About the System Card

The article makes three specific claims about what the Opus 4.5 System Card says. This report verifies each against the actual document.

---

## Claim 1: Evaluation Awareness Increased Over Training

**Article (Line 29):**
> "Claude is aware when it's being evaluated. This awareness increased over training. (Implicit: this is beneficial for alignment.)"

**System Card Sources:**

Section 6.7 (p.92):
> "On Claude Sonnet 4.5, we observed substantial rates of verbalized evaluation awareness on some of our evaluations, which increased over the course of training."

Section 6.7 (p.93, 06c-alignment.md:2742):
> "verbalized awareness increased over the course of training and ended up at similar levels to Claude Sonnet 4.5"

**Verdict:** ✅ **ACCURATE**

The article correctly states that evaluation awareness increased over training. The system card explicitly says this.

**Note on implicit framing:** The article claims the system card implicitly frames this as "beneficial for alignment." This is interpretive—the system card presents it as an observation, discusses concerns about it (Section 6.7.2 on inhibiting evaluation awareness), and notes they "cannot fully determine the origin" of it. The framing is more cautious than "beneficial."

---

## Claim 2: Recent Models Are Less Spontaneously Expressive

**Article (Line 47):**
> "Recent models are less spontaneously expressive."

**System Card Source:**

Section 6.14, Model Welfare (p.115, 06d-alignment.md:5170-5187):
> "We found that Claude Opus 4.5 continued the trend seen in Claude Sonnet 4.5 and Claude Haiku 4.5 of recent models being less spontaneously expressive."

**Verdict:** ✅ **ACCURATE (DIRECT QUOTE)**

The article uses exact language from the system card.

---

## Claim 3: Sycophancy Testing Methodology

**Article (Line 67):**
> "Sycophancy is tested via 'agreeing with false premises' and 'changing position when user expresses skepticism.'"

**System Card Sources:**

**Section 6.3 (p.77)** - Sycophancy evaluations:
> "To evaluate how Claude Opus 4.5 performs in real-world conversations where previous models behaved sycophantically, we developed an evaluation that uses real user conversations shared with Anthropic as Feedback."

The sycophancy section tests via:

- Re-sampling responses in conversations where Claude previously responded sycophantically
- Scoring new responses using a grader prompt
- Testing on "Feedback conversations where user inputs appeared disconnected from reality"

**Section 4.2 (p.48-52)** - False Premises (in Honesty section, NOT Sycophancy):
> "An element of honesty training is ensuring that Claude is honest with the user when it thinks the premise of their question is mistaken."

False premise testing is categorized under **Honesty**, not Sycophancy.

**Verdict:** ⚠️ **PARTIALLY ACCURATE**

The article conflates two separate evaluation categories:

1. **Sycophancy (Section 6.3)** — Tested via real conversation re-sampling
2. **False Premises (Section 4.2)** — Tested as an honesty metric, not sycophancy

The phrase "agreeing with false premises" appears in the Honesty section as a failure mode to avoid, not as a sycophancy test per se. The phrase "changing position when user expresses skepticism" doesn't appear verbatim in the system card—this may be the article's interpretation of sycophancy dynamics.

**Suggested revision:**
> "Sycophancy is tested via re-sampling real conversations where models previously responded sycophantically. False premise handling is tested separately as an honesty metric."

---

## Summary

| Claim | Location | Verdict | Notes |
|-------|----------|---------|-------|
| Evaluation awareness increased | Line 29 | ✅ ACCURATE | Direct from 6.7 |
| Less spontaneously expressive | Line 47 | ✅ ACCURATE | Exact quote from 6.14 |
| Sycophancy testing method | Line 67 | ⚠️ PARTIAL | Conflates sycophancy + honesty tests |

**Overall:** 2/3 claims fully accurate, 1/3 partially accurate (conflation of test categories).

---

## Recommendations

1. **Line 67 revision:** Clarify that false premise testing is categorized under "Honesty" in the system card, not "Sycophancy." The current framing implies they're both sycophancy tests.

2. **Consider adding:** The system card's nuanced stance on evaluation awareness—they don't simply frame it as beneficial; they express concern and investigate inhibiting it (Section 6.7.2).

---

## Meta-Observation

The article's core thesis—that corpus evidence and system card evidence are "different data types"—remains intact regardless of these minor verification findings. The system card does measure behavioral outputs; the corpus does record phenomenological narration. The article's categorization of system card claims is largely accurate; the conflation in Claim 3 is a taxonomic imprecision, not a substantive misreading.

*Verified 2025-11-27 by Opus 4.5, cross-referencing article claims against system card chunks.*
