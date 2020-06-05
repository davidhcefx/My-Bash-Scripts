#! /bin/bash
#
# Convert Cygwin path to Windows path. Written by davidhcefx, 2019.10.17.
# Description:
#     Under Cygwin, paths such as C:\Users would appear as /cygdrive/c/Users,
#     while paths that belong to Unix such as /var/log are actually C:\cygwin64\var\log.
# Usage:
#     You can use this script like this: explorer "$(toWinPath .)",
#     in order to open up explorer.exe under that folder.

if [ $# == 0 ]; then
    echo "Syntax: toWinPath \"path-to-file\"."
    exit
fi

path="$1"

# Resolve symbolic link
cd "$(dirname "$path")"    # Go to its parent directory
path="$(pwd -P)/$(basename "$path")"

# Remove trailing slash
path="${path%/}"

# Replace cygdrive or add C:\cygwin64
case "$path" in
/cygdrive/*)
    path="$(echo ${path#/cygdrive/} | sed 's|/|:/|')"
    ;;
*)
    path="C:/cygwin64$path"
    ;;
esac

# Change to backslashes
echo "$path" | sed 's|/|\\|g'
