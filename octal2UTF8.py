#! /usr/bin/env python3
from sys import argv
"""
    Convert octal-string to UTF8 string. Written by davidhcefx, 2023.10.27

    $ ./octal2UTF8.py '\147\144\142\347\204\241\346\263\225\351\241\257\347\244\272\347\232\204\344\270\255\346\226\207\345\255\227'
gdb無法顯示的中文字
"""

def encode(utf8: str) -> str:
    bt = utf8.encode()
    return '\\' + '\\'.join(map(lambda b: oct(b)[2:], bt))


def decode(octalstr: str) -> str:
    bt = bytearray()
    bt.extend(map(
        lambda s: int(s, 8),
        filter(len, octalstr.split('\\'))))

    return bt.decode(encoding='utf8')


if __name__ == '__main__':
    if len(argv) > 1:
        res = decode(argv[1])
    else:
        res = decode(input('Octal string input (eg. \\xxx\\yyy): '))

    print(res)
