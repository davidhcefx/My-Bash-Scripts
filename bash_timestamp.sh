#! /bin/bash
#
# Please set up to run this script upon user login.

printf "\n[-- System Login: $USER@`uname -n`, $(date +%-m/%-d:%H) --]\n\n" >> ~/.bash_history
