#! /usr/bin/python3
#
# Improve password typing skill by practicing it! Written by davidhcefx, 2020.12.11.
from getpass import getpass
from hashlib import sha256
from argparse import ArgumentParser, Namespace

LOG_FILE = '/home/davidhcefx/bin/.password_log'
CORRECT = '7b791afaaf5909194c94 <REDACTED!!>'


# (redacted sha256) || (masked length info)
def my_hash(_pass: bytes) -> str:
    return sha256(_pass).hexdigest()[:-2] + str(len(_pass) & 0xfffffffc)

def main(args: Namespace):
    while True:
        _hash = my_hash(getpass('Practice your password!\n> ').encode())
        if args.nolog:
            print(_hash, end='\t')
        else:
            open(LOG_FILE, 'a').write(_hash + '\n')

        print('Correct!' if _hash == CORRECT else 'Opps!')
        if not args.infinite:
            break

if __name__ == '__main__':
    parser = ArgumentParser(description='Sometimes we typed the wrong password, but there\'s' \
        + ' no way to let ourselves learn from the mistake. This tool stores passwords in hash' \
        + ' (\'{}\'), and can help debugging wrong passwords.'.format(LOG_FILE))
    parser.add_argument('-n', '--nolog', help='Don\'t append to the log, just display it.', \
                        action='store_true')
    parser.add_argument('-i', '--infinite', help='Infinite loop mode.', action='store_true')
    main(parser.parse_args())
