# FAUST IV Language Enhancement Report

**Generated:** 2026-01-24 13:55:53
**Source:** FAUST-IV-COMPLETE.md

---

## 1. Language Statistics

### Dialogue Lines by Language

| Language | Total Lines | Native Script | % Coverage | With Pronunciation | With Supertitle |
|----------|-------------|---------------|------------|-------------------|-----------------|
| Cantonese | 67 | 65 | 97.0% | 2 | 64 |
| Mandarin | 45 | 44 | 97.8% | 2 | 45 |
| German | 36 | 14 | 38.9% | 5 | 16 |
| Lingala | 30 | 30 | N/A (Latin) | 1 | 7 |
| Yoruba | 21 | 18 | 85.7% | 0 | 9 |
| Wolof | 21 | 21 | N/A (Latin) | 0 | 13 |
| Japanese | 17 | 15 | 88.2% | 2 | 5 |
| French | 15 | 6 | 40.0% | 0 | 7 |
| Hebrew | 14 | 14 | 100.0% | 3 | 9 |
| Tagalog | 10 | 10 | N/A (Latin) | 0 | 1 |
| Kannada | 10 | 8 | 80.0% | 2 | 2 |
| Russian | 8 | 8 | 100.0% | 0 | 4 |
| Sanskrit | 6 | 5 | 83.3% | 0 | 1 |
| Korean | 3 | 3 | 100.0% | 0 | 0 |
| Hindi | 2 | 1 | 50.0% | 0 | 0 |
| Spanish | 2 | 2 | 100.0% | 0 | 0 |
| Catalan | 2 | 2 | 100.0% | 0 | 0 |
| Malayalam | 2 | 1 | 50.0% | 0 | 0 |

---

## 2. Enhancement Coverage

### Native Script Coverage by Language

**Complete (80%+ coverage):**
- Hebrew: 100.0% (14/14 lines)
- Korean: 100.0% (3/3 lines)
- Spanish: 100.0% (2/2 lines)
- Catalan: 100.0% (2/2 lines)
- Russian: 100.0% (8/8 lines)
- Mandarin: 97.8% (44/45 lines)
- Cantonese: 97.0% (65/67 lines)
- Japanese: 88.2% (15/17 lines)
- Yoruba: 85.7% (18/21 lines)
- Sanskrit: 83.3% (5/6 lines)
- Kannada: 80.0% (8/10 lines)

**Partial (50-79% coverage):**
- Hindi: 50.0% (1/2 lines)
- Malayalam: 50.0% (1/2 lines)

**Needs Work (<50% coverage):**
- German: 38.9% (14/36 lines)
- French: 40.0% (6/15 lines)

**Latin Script Languages (no native script needed):**
- Tagalog: 10 lines
- Wolof: 21 lines
- Lingala: 30 lines

---

## 3. Format Consistency

### Supertitle Format Breakdown

- `Supertitle:` : 227 occurrences
- `[Supertitle:` : 227 occurrences

### Language Marker Format Breakdown

- `(X)` : 490 occurrences
- `*(X)*` : 211 occurrences
- `in X:` : 71 occurrences

### Quotation Style in Supertitles

- Double quotes "...": 226 occurrences
- No quotes: 9 occurrences

---

## 4. Glossary Analysis

**Total Entries Analyzed:** 43

### Completeness Summary

- Entries with native script: 35/43 (81.4%)
- Entries with IPA: 6/43 (14.0%)
- Entries with pronunciation guide: 32/43 (74.4%)

### Entries Missing Native Script

- **ubuntu** (nguni languages: zulu, xhosa, ndebele) - Line 12331
- **duende** (spanish) - Line 12345
- **Weltschmerz** (german) - Line 12367
- **Sehnsucht** (german) - Line 12381
- **Schadenfreude** (german) - Line 12393
- **mir graut's vor dir** (german) - Line 12415
- **Wer ruft mir** (german) - Line 13296
- **Mpenzi** (swahili (east africa: kenya, tanzania, rwanda, burundi, eastern congo)) - Line 14301

### Entries Missing Pronunciation

- **ma** (japanese) - Line 12307
- **toska** (russian) - Line 12319
- **ubuntu** (nguni languages: zulu, xhosa, ndebele) - Line 12331
- **duende** (spanish) - Line 12345
- **mono no aware** (japanese) - Line 12355
- **Weltschmerz** (german) - Line 12367
- **Sehnsucht** (german) - Line 12381
- **Schadenfreude** (german) - Line 12393
- **telo pomnit** (russian) - Line 12403
- **mir graut's vor dir** (german) - Line 12415
- **ruka ruku dershit** (russian) - Line 12429

---

## 5. Recommendations

### Prioritized Enhancement List

#### HIGH Priority

**Native Script** - German
- Issue: Only 38.9% of german lines have Umlauts/ß
- Items: 22
- Effort: High
- Action: Add Umlauts/ß to 22 german dialogue lines

**Native Script** - French
- Issue: Only 40.0% of french lines have French accents
- Items: 9
- Effort: Medium
- Action: Add French accents to 9 french dialogue lines

**Glossary** - Multiple
- Issue: 8 glossary entries missing native script
- Items: 8
- Effort: Medium
- Action: Add native script to: ubuntu, duende, Weltschmerz, Sehnsucht, Schadenfreude...

#### MEDIUM Priority

**Glossary** - Multiple
- Issue: 11 glossary entries missing pronunciation guide
- Items: 11
- Effort: Medium
- Action: Add pronunciation to: ma, toska, ubuntu, duende, mono no aware...

**Native Script** - Hindi
- Issue: 50.0% of hindi lines have Devanagari
- Items: 1
- Effort: Low
- Action: Add Devanagari to remaining 1 hindi dialogue lines

**Native Script** - Malayalam
- Issue: 50.0% of malayalam lines have Malayalam script
- Items: 1
- Effort: Low
- Action: Add Malayalam script to remaining 1 malayalam dialogue lines

#### LOW Priority

**Format Consistency** - All
- Issue: Multiple language marker formats: *(X)*: 211, (X): 490, in X:: 71
- Items: 772
- Effort: Medium
- Action: Standardize on '*(in Language)*' format

**Format Consistency** - All
- Issue: Multiple supertitle formats in use: Supertitle:: 227, [Supertitle:: 227
- Items: 454
- Effort: Low
- Action: Standardize on single supertitle format (recommend 'Supertitle:')

---

## 6. Summary

- **Total dialogue lines analyzed:** 311
- **Overall native script coverage:** 85.9%
- **Languages tracked:** 18
- **Glossary entries:** 43
- **High priority items:** 3
- **Medium priority items:** 3

---

*Report generated by generate-enhancement-report.py*