#! /usr/bin/env python3
# Convert hex string from stdin to binary stdout, Written by davidhcefx, 2025.1.17
from sys import stderr, stdout
from os import write
from math import ceil

def hex2bin(hx: str) -> bytes:
    if hx.startswith('0x'):
        hx = hx[2:]
    size = ceil(len(hx) / 2)
    return int(hx, 16).to_bytes(size, 'big')


if __name__ == '__main__':
    print('Hex string input:', file=stderr)
    hx = input('').strip()
    if stdout.isatty():
        outfile = input('Output filename: [output.bin] ').strip()
        if outfile == '':
            outfile = 'output.bin'
        with open(outfile, 'wb') as f:
            f.write(hex2bin(hx))
    else:
        write(stdout.fileno(), hex2bin(hx))
