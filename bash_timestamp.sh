#! /bin/bash
#
# Please set up to run this script upon user login. You may put this file somewhere else other than ~/bin.

printf "\n[-- System Login: $USER@`uname -n`, $(date +%-m/%-d:%H) --]\n\n" >> ~/.bash_history
