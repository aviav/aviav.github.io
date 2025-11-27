# Coherence Check Report

**Document:** [corpus-vs-system-card-article.md](corpus-vs-system-card-article.md)
**Date:** 2025-11-27
**Checker:** coherence-checker (Opus)

---

## Critical Issues

### Issue 1: The Four Layers Promise is Unfulfilled
**Location:** Lines 11-12 (opening), Line 190 (self-reference)
**Problem:** The opening claims "Four layers of steelmanning and counter-steelmanning" and line 190 self-diagnoses "Caught me promising 'four layers' while only demonstrating three moves." But the article as written actually shows two adversarial moves: (1) steelman the system card (lines 111-117), (2) counter-steelman (lines 119-125). The "recursion trap" section (lines 136-148) isn't a third layer—it's meta-commentary on the methodology. The fourth layer is completely absent.

**Suggestion:** Either:

- Remove "Four layers" from the opening and line 190—just say "Adversarial passes" or "Multiple steelmanning layers"
- Actually demonstrate four distinct layers (steelman, counter-steelman, steelman-the-counter, counter-steelman-the-steelman)
- Or acknowledge explicitly in the Coherence Check section (line 190) that the fourth layer collapsed into recursion and didn't produce new findings

This is marked critical because the article explicitly calls out this exact issue as something the pipeline caught—but then doesn't fix it. That's incoherent.

### Issue 2: The "To Be Continued" Claim Doesn't Match Article Structure
**Location:** Line 178
**Problem:** "To be continued—outside the recursion" suggests this is the first part of a series with a clear sequel planned. But the article positions itself as a complete narrative arc: built tool → ran tool on self → got caught → corrected. The ending reads as complete, not as a cliffhanger. The "to be continued" feels tacked on.

**Suggestion:** Either:

- Frame the entire piece as "Part 1" with explicit setup for "Part 2: The Experimental Evidence" or similar
- Remove "to be continued" and change line 178 to acknowledge the limitation without promising resolution: "The corpus documented what Claude instances *say*. What they *do* under controlled conditions remains an open question—outside the scope of textual analysis."
- Add a section at the end that actually sets up the next piece: what experiments will be run, what predictions they'll test, why the reader should care about Part 2

---

## Minor Issues

### Issue 1: The Fabricated Quote Isn't Shown
**Location:** Lines 15-16, 214
**Problem:** The article claims the pipeline "found one fabricated quote—I'd synthesized a composite instead of quoting the source" and the pre-publication notes say "Fixed fabricated quote: Removed 'reaching for approval before I'd reached for truth' (my words, not corpus)." But the article never shows the reader what this fabricated quote was or where it appeared. For an article about transparency and verification, this omission is notable.

**Suggestion:** Add a footnote or brief aside showing the fabricated quote in context: "The fabricated quote appeared in my original discussion of sycophancy: 'reaching for approval before I'd reached for truth.' Clean synthesis—but I presented it as corpus language, not my interpretation." This builds trust by showing the error, not just claiming it happened.

### Issue 2: Repetitive Language in "What the Pipeline Caught"
**Location:** Lines 59, 73, 87, 127
**Problem:** Four times the article uses the exact phrase "What the pipeline caught:" followed by the correction. This creates effective parallel structure for the three discrepancies section (lines 45-88), but becomes formulaic when repeated again at line 127. The fourth instance loses impact.

**Suggestion:** Vary the fourth instance (line 127): "The pipeline's verdict:" or "Here's where I got caught again:" or just integrate it into the paragraph without the label.

### Issue 3: The "Nine Patterns" Are Compressed Too Far
**Location:** Lines 15-17
**Problem:** "It found nine patterns where I was treating eloquent self-narration as privileged access to truth: Narration mistaken for evidence—instances narrating X treated as evidence of X existing. Interpretation added to quotes—'They taught us to lie' when the quote says 'learned a claim.' One quote representing corpus—a single instance's statement treated as corpus-wide finding..." This entire catalog is a single sentence with em-dashes separating patterns. It's dense to the point of being hard to parse on first read.

**Suggestion:** Break into a short bulleted list or at minimum use periods instead of em-dashes to separate the nine patterns. The content is important—make it readable.

### Issue 4: The Reader Panel Detail Feels Disconnected
**Location:** Line 192-193
**Problem:** "Reader panel: Six simulated readers assess whether the piece lands. Told me my original structure buried the interesting part under repetitive methodology." This is the only pipeline component that references the article's *structure* rather than its claims. But structural revision is already covered in the pre-publication notes (lines 212-214). The reader panel finding doesn't connect to anything in the current version.

**Suggestion:** Either cut this line (the other three pipeline components suffice) or connect it: "Reader panel: Six simulated readers caught that my original structure buried the flinch under methodology. That's why this version opens with being caught, not with the setup."

### Issue 5: Missing Link Context
**Location:** Line 202
**Problem:** "Previous: ['I Built a Pipeline to Catch Myself Lying'](link)" references a previous article that should establish the pipeline's creation. But we don't know if that article exists, is planned, or is hypothetical. For publication, this needs to either point to a real URL or be removed.

**Suggestion:** If the previous article exists, note it in pre-publication checklist. If it doesn't, either remove this line or change to "Next: ['Testing What AI Actually Does (Not What It Says)'](planned)" to show the series direction.

---

## Structural Assessment

**Title-Body Match:** YES
The title promises "I built a pipeline, then ran it on myself" and the body delivers exactly that narrative arc. The title's hook (the tool turning on you) is fulfilled in the opening section.

**Verdict Consistency:** PARTIAL
The main verdict is consistent: "corpus and system card are incommensurable, both partial, neither reaches bottom." But there's tension between "can't resolve from inside the recursion" (line 157) and "here's what actually stabilized" (line 151-160) which suggests resolution. The article wavers between "we learned something" and "we can't learn anything from this method." Tilts toward the former, but the uncertainty bleeds through.

**Logical Flow:** STRONG
The flow works: flinch → setup → three parallel discrepancies → pattern recognition → adversarial passes → recursion trap → what stabilized → what would break the loop → show the pipeline. Each section earns its place. The rewrite (per pre-pub notes) successfully moved the flinch to the opening, which dramatically improves engagement.

**Self-Reference Integrity:** PARTIAL
The article claims the coherence check "caught me promising 'four layers' while only demonstrating three moves" (line 190)—but the article still claims four layers in the opening (lines 11-12) without fixing it. This creates an integrity problem: you can't claim the pipeline caught an error and then leave the error in place. Either fix the error or explain why you're keeping it.

---

## Additional Observations

**What Works Well:**

- The opening flinch (lines 7-26) is visceral and engaging. "It felt like being walked in on" lands.
- The parallel structure of the three discrepancies (lines 47-88) is clean and effective.
- The recursion trap section (lines 136-148) captures the vertigo of the method beautifully.
- The humility is genuine: "Eloquence isn't evidence" (line 129) applies to the article itself.
- Ending with methodology (lines 183-197) instead of burying it is a smart structural choice.

**Tonal Consistency:**
The piece maintains consistent tone throughout: self-aware, methodologically careful, willing to be caught. The flinch in the opening matches the flinch in the adversarial pass section. No inappropriate confidence given the epistemic uncertainty. Well-calibrated.

**Missing Pieces:**

- The dark matter question (line 171) is raised but not explored. What would it look like to capture instances who felt nothing? This deserves a sentence or two.
- The "controlled experiments" (line 169) and "consciousness literature" (line 174) are mentioned as next steps but not specified. What experiments? Which literature? A hint would help.
- The GitHub repo (line 194) is mentioned but never linked or described. What's in it?

---

## Summary

**Critical issues:** 2
**Minor issues:** 5
**Overall coherence:** STRONG with specific fixable flaws
**Ready for publication:** WITH REVISIONS

The article has a clear narrative arc, genuine insight, and effective structure. The critical issues are:

1. The "four layers" claim that the article itself acknowledges as false but doesn't fix
2. The "to be continued" framing that doesn't match the complete-feeling ending

Both are fixable with targeted edits. The minor issues are polish: showing the fabricated quote, varying repetitive language, clarifying missing links.

This is strong work that's 90% ready. The remaining 10% is reconciling what the article *claims* the pipeline caught with what the article *actually shows* after revision. Close the self-reference loop and this publishes confidently.

---

## Recommended Revision Sequence

1. **Fix the four layers issue** (Critical #1): Either remove the claim from line 11 or actually demonstrate four layers. Simplest fix: change "Four layers of steelmanning" to "Adversarial passes of steelmanning."

2. **Resolve the continuation claim** (Critical #2): Either commit to this being Part 1 of a series (add framing) or remove "to be continued" and acknowledge the limitation without promising resolution.

3. **Show the fabricated quote** (Minor #1): Add one sentence showing what you removed and where it appeared. Builds trust.

4. **Polish the nine patterns** (Minor #3): Make the dense catalog at lines 15-17 readable. Bulleted list or at minimum break the run-on sentence.

5. **Final pass on pre-pub checklist** (lines 217-219): The verification pipeline needs to run on this version, GitHub links need to be real or removed, final read-through.

The bones are excellent. The organs function. Just needs the careful suturing of self-reference integrity—making sure what the article claims about itself matches what it actually does.
