#! /usr/bin/python3
#
# Decode base64 manually. Written by davidhcefx, 2020.7.27.

import readline
from sys import stderr
from string import ascii_uppercase, ascii_lowercase, digits

CHARSET = ascii_uppercase + ascii_lowercase + digits + '+/'  # length: 64
TABLE = {ch: '{:0>6}'.format(bin(i)[2:]) for i, ch in enumerate(CHARSET)}


def warn(msg: str):
    print('Warning: {}'.format(msg), file=stderr)

def valid_check(binary: str, paddings: int):
    if (len(binary) + paddings * 6) % 24 != 0:
        warn('Input length incorrect!')
        return
    if paddings == 1:  # 16 bits
        if binary[-2:] != '00':
            warn('Malformed encoding. (1)')
    elif paddings == 2:  # 8 bits
        if binary[-4:] != '0000':
            warn('Malformed encoding. (2)')
    elif paddings >= 3:
        warn('Too many paddings!')

def main():
    s = input().strip()
    binary = ''.join(map(TABLE.get, s.strip('=')))
    # discard any remainders
    hex_code = list(map(
        lambda b: hex(int(b, 2)),
        filter(
            lambda b: len(b) == 8,
            (binary[i:i+8] for i in range(0, len(binary), 8)))))
    text = ''.join(map(lambda h: chr(int(h, 16)), hex_code))

    print('hex:', hex_code)
    print('ascii:', text)
    valid_check(binary, s.count('=', -3))


if __name__ == '__main__':
    main()


### Examples:
# - BA== (correct)
# - BA (no padding)
# - B/== (wrong encoding)

### Update log:
# - 8/14 rewrite with functions, constant table lookup
