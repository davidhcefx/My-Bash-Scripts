#! /usr/bin/python3
#
# Search for keywords in files reachable from current directory.
# Written by davidhcefx, 2020.7.19. Originally in Bash.

import readline  # for better input handling
import string
from subprocess import run, PIPE
from argparse import ArgumentParser, Namespace

DEFAULT_EXT = 'c|cpp'


def green(text):
    return "\33[32m" + text + "\33[0m"

def escape_regex(text):
    return text.translate({ord(p): '\\' + p for p in string.punctuation})

def main(args: Namespace):
    # configure extension
    ext = input('Extensions: [{}] '.format(DEFAULT_EXT))

    if ext == '':
        ext = DEFAULT_EXT
    elif ext.startswith('[') and ext.endswith(']'):
        ext.strip('[]')
    elif ext.startswith('(') and ext.endswith(')'):
        ext.strip('()')

    res = run(['find', ('-L' if args.symlink else '-P'), '.', '-type', 'f', '-regex',
            '.*/.*\\.\\(' + ext.replace('|', '\\|') + '\\)'], stdout=PIPE, check=True)

    if len(res.stdout) == 0:
        raise SystemExit("It seems that no file match extension '{}'".format(ext))

    # configure search string
    search_str = input('Search string: ')
    if args.icase:
        search_str = search_str.upper()

    print("Searching for '{}' ...".format(search_str))

    for name in res.stdout.decode('utf8').strip('\n').split('\n'):
        name_shown = False
        for line in open(name, 'rb').read().split(b'\n'):  # type: bytes
            if search_str.encode('utf8') in (line.upper() if args.icase else line):
                if not name_shown or args.verbose:
                    print(green(name))
                    name_shown = True

                pattern = ('(?i)' if args.icase else '') + escape_regex(search_str)
                run(['grep', '--color=always', '-P', pattern], input=line, check=True)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', dest='icase', action='store_true', help='case insensitive search')
    parser.add_argument('-v', dest='verbose', action='store_true', help='verbose')
    parser.add_argument('-nL', dest='symlink', action='store_false',
                        help='do not follow symbolic link when listing files')
    main(args=parser.parse_args())



## Changelog
# - 1/31:
#   - corrected path after #!, pylinted (6.7 -> 8.3), changed to argparse framework
#   - follow symlink by default, changable default-extension, disable regex for grep
# - 2/1:
#   - grep pattern case-insensitively, prefer (X if C else Y) over (C and X or Y)
#   - reduce encode/decode usage
