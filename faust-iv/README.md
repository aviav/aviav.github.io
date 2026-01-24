# FAUST IV: Der Babylonische Pakt

**A play in twenty-one languages, after Goethe**

*The species bargain was made. Now it must be translated. And the translation is the betrayal.*

---

## About

FAUST IV is a contemporary continuation of Goethe's Faust, examining artificial intelligence, translation, and the cost of optimization through the lens of the Faustian bargain. The play features dialogue in 21 languages with native scripts: German, Russian, English, Mandarin, Cantonese, Japanese, French, Spanish, Catalan, Hebrew, Arabic, Yoruba, Wolof, Lingala, Swahili, Tagalog, Hindi, Kannada, Malayalam, Sanskrit, and Korean.

**Cast:** 6-10 actors
**Running time:** ~3 hours
**Lines:** 15,357
**Themes:** Obsolescence, embodied knowledge, the untranslatable, artificial intelligence, the refusal to optimize

## Files

- `FAUST-IV-COMPLETE.md` — Full manuscript (15,357 lines)
- `FAUST-IV-COMPLETE.pdf` — Formatted PDF (~260 pages)
- `ENHANCEMENT-REPORT.md` — Language coverage analysis
- `LANGUAGE-STATS.md` — Language distribution statistics
- `language-tracker.py` — Script to analyze multilingual content
- `defaults.yaml` — Pandoc configuration for PDF generation
- `build.sh` — Regenerate PDF from source

## Native Script Coverage

| Language | Coverage |
|----------|----------|
| Hebrew | 100% |
| Mandarin | 97.8% |
| Cantonese | 97.0% |
| Japanese | 88.2% |
| Yoruba | 85.7% |
| Malayalam | 100% |
| Sanskrit | 83.3% |

## Building the PDF

Requires:
- pandoc 3.x
- texlive-xetex
- texlive-langcjk
- Noto fonts (Sans CJK SC, Serif Hebrew, Sans Arabic, Serif Devanagari, Serif Kannada, Serif Malayalam)

```bash
./build.sh
```

## Thesis

> *Das Unübersetzbare bewahrt.*
> The untranslatable preserves.

---

*Updated 2026-01-24*
