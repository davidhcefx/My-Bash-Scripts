# tee-safe - Tee with Prompting

- Ever have this catastrophic experience using `tee` to accidentally overwritten some files and couldn't fully recover it? To prevent it from happening again, you need this script!


## Installation

1. Put this file (`tee-safe`) under your `~/bin` folder.

2a. If you are on Linux, please ensure that [Zenity](https://packages.ubuntu.com/search?keywords=zenity) has been installed.

2b. If you are on Windows, please install [MessageBox](https://github.com/davidhcefx/Windows-MessageBox-for-Cmd) first. After that, comment out [Lines 8 to 14](https://github.com/davidhcefx/My-Bash-Scripts/blob/d7eacbb2fffa5d9c84b25831dbbfb76071028261/tee-safe%20-%20Tee%20with%20Prompting/tee-safe#L8-L14) within the script.

3. Finally, you can set up aliases like `alias tee='tee-safe'` to wrap up the original one.

## Linux

<img src="scnshot.png" width=600>

## Windows

<img src="scnshot2.png" width=600>
