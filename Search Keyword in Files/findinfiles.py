#! /usr/bin/python3
#
# Search for keywords in files reachable from current directory.
# Written by davidhcefx, 2020.7.19. Originally in Bash.

import readline  # for better input handling
import string
from subprocess import run, PIPE
from argparse import ArgumentParser, Namespace

DEFAULT_EXT = 'h c cpp'


def cyan(text: str) -> str:
    return '\33[36m' + text + '\33[0m'

def green(text: str) -> str:
    return '\33[32m' + text + '\33[0m'

def escape_regex(text: str) -> str:
    return text.translate({ord(p): '\\' + p for p in string.punctuation})

def main(args: Namespace):
    # configure extension
    ext = input('Extensions: [{}] '.format(DEFAULT_EXT)) or DEFAULT_EXT
    ext = list(map(lambda x: '\\.' + x.strip('.'), ext.split()))  # remove dots if exists
    regex = '.*\\({}\\)'.format('\\|'.join(ext))
    res = run(['find', '-L' if args.symlink else '-P', '.', '-type', 'f', '-regex', regex],
              stdout=PIPE,
              check=True)
    if len(res.stdout) == 0:
        raise SystemExit('It seems that no file match extension "{}"'.format(ext))

    # configure search string
    search_str = input('Search string: ')
    grep_pattern = '{}{}'.format('(?i)' if args.icase else '', escape_regex(search_str))
    print('Searching for "{}" ...'.format(search_str))

    for name in res.stdout.decode('utf8').strip('\n').split('\n'):
        r = run(['grep', '--color=always', '-n', '-P', grep_pattern, name], stdout=PIPE)
        if len(r.stdout) > 0:
            print(cyan(name))
            print(r.stdout.decode('utf8'), end='')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', dest='icase', action='store_true', help='case insensitive search')
    parser.add_argument('-nL', dest='symlink', action='store_false',
                        help='do not follow symbolic link when listing files')
    main(parser.parse_args())



## Changelog
# - 1/31:
#   - corrected path after #!, pylinted (6.7 -> 8.3), changed to argparse framework
#   - follow symlink by default, changable default-extension, disable regex for grep
# - 2/1:
#   - grep pattern case-insensitively, prefer (X if C else Y) over (C and X or Y)
#   - reduce encode/decode usage
# - 6/8:
#   - change extension representation to .h, show line number
# - 6/11:
#   - simply use grep to do all the stuff
# - 2/8:
#   - simplify what needed to be entered as extensions, correct `-regex` option usage.
