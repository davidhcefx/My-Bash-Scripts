#! /bin/python3
#
# Search for keywords in files reachable from current directory.
# Written by davidhcefx, 2020.7.19. Originally in Bash.

from sys import argv
from os.path import basename
import readline
from subprocess import run, PIPE


VERBOSE = False
INSENSITIVE = False

def help():
    print(f'Syntax: {basename(argv[0])} (-i|-v|-h)')
    print('\t-i:\tCase insensitive search.')
    print('\t-v:\tVerbose.')
    print('\t-h:\tHelp.')

def green(text):
    return "\33[32m" + text + "\33[0m"

def main():
    # configure extension
    ext = input('Extensions: [c|cpp] ')

    if ext == '':
        ext = 'c|cpp'
    elif ext.startswith('[') and ext.endswith(']'):
        ext.strip('[]')
    elif ext.startswith('(') and ext.endswith(')'):
        ext.strip('()')

    r = run(['find', '.', '-type', 'f', '-regex',
            '.*/.*\\.\\(' + ext.replace('|', '\\|') + '\\)'], stdout=PIPE)
    r.check_returncode()

    if len(r.stdout) == 0:
        print(f"It seems that no file match extension '{ext}'")
        exit(1)

    # configure search string (format: bytes)
    search_str = input('Search string: ').encode('utf8')
    if INSENSITIVE:
        search_str = search_str.upper()

    print("Searching for '" + search_str.decode('utf8') + "' ...")

    for name in r.stdout.decode('utf8').strip('\n').split('\n'):
        name_shown = False
        for line in open(name, 'rb').read().split(b'\n'):
            if search_str in ((INSENSITIVE and line.upper()) or line):
                if not name_shown or VERBOSE:
                    print(green(name))
                    name_shown = True
                run(['grep', '--color=always', search_str], input=line)


if __name__ == '__main__':
    if len(argv) > 1:
        for arg in argv[1:]:
            if arg == '-i':
                INSENSITIVE = True
            elif arg == '-v':
                VERBOSE = True
            elif arg == '-h':
                help()
                exit(0)
    main()
