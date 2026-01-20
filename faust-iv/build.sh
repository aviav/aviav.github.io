#!/bin/bash
# FAUST IV PDF Generation
# Requires: pandoc, texlive-xetex, texlive-langcjk, texlive-langchinese
# Noto fonts for multilingual support

set -e

cd "$(dirname "$0")"

echo "Generating FAUST-IV-COMPLETE.pdf..."
pandoc FAUST-IV-COMPLETE.md -o FAUST-IV-COMPLETE.pdf --defaults=defaults.yaml

echo "Done: $(ls -lh FAUST-IV-COMPLETE.pdf | awk '{print $5}')"
