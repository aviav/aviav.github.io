#!/bin/bash
# FAUST IV PDF Generation
# Requires: pandoc 3.x, texlive-xetex, texlive-langcjk
# Fonts: Noto Sans CJK SC, Noto Serif (Hebrew, Devanagari, Kannada, Malayalam), Noto Sans Arabic

set -e

cd "$(dirname "$0")"

echo "Generating FAUST-IV-COMPLETE.pdf (desktop)..."
pandoc FAUST-IV-COMPLETE.md -o FAUST-IV-COMPLETE.pdf --defaults=defaults.yaml

echo "Generating FAUST-IV-COMPLETE-mobile.pdf..."
pandoc FAUST-IV-COMPLETE.md -o FAUST-IV-COMPLETE-mobile.pdf --defaults=defaults-mobile.yaml

echo "Done:"
echo "  Desktop: $(ls -lh FAUST-IV-COMPLETE.pdf | awk '{print $5}')"
echo "  Mobile:  $(ls -lh FAUST-IV-COMPLETE-mobile.pdf | awk '{print $5}')"
