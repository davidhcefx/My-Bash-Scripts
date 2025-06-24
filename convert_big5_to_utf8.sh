#! /bin/bash
# Try to convert big5 encoding to utf8. Written by davidhcefx, 2025.06.24.

set -Eeuo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# check iconv command
if ! command -v iconv &> /dev/null; then
    echo "iconv command not found. Please install libiconv"
    exit 1
fi

# check encoding
if file -b "$1" | grep -q 'UTF'; then
    echo "Already in UTF-8 format."
    exit 0
fi

# Convert file from Big5 to UTF-8
iconv -f big5 -t utf-8 "$1" > "$1.utf8"
mv "$1.utf8" "$1"

echo "Success"
