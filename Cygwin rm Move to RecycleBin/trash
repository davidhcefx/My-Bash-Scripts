#! /bin/bash
#
# A rm replacement on Cygwin, using Recycle.exe (http://www.maddogsw.com/cmdutils/).
# Created by davidhcefx, 2019.11.8.

files=()
retVal=0

if [[ $# == 0 ]]; then
    cmd.exe /c Recycle /?
    exit
fi

for f in "$@"; do
    case "$f" in
    -r)  # obmit -r
    ;;
    *)
        if [[ -e "$f" ]]; then
            files+=("$(toWinPath "$f")")
        else
            echo "trash: cannot remove '$f': No such file or directory"
            retVal=1
        fi
    ;;
    esac
done

cmd.exe /c Recycle -f "${files[@]}" || retVal=$?
exit $retVal
