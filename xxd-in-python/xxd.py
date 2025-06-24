#! /usr/bin/env python3
# Tool to mimic xxd(1). Written by davidhcefx, 2025.4.9
from sys import argv, stderr
from string import ascii_letters, digits, punctuation

PRINTABLE = set((ascii_letters + digits + punctuation + ' ').encode())


def xxd_revert(fname: str, cols: int = 16) -> None:
    """
    fname: file name
    cols: octets per line in input

    Each line should be in format
    00000000: 2321 202f 7573 722f 6269 6e2f 656e 7620  #! /usr/bin/env
    """
    with open(fname, 'r') as f:
        line = f.readline()
        while line and line[8:].startswith(': '):
            # extract cols octets
            line = line[10:]
            line = line[:cols * 2 + cols // 2 - 1]
            b = bytes.fromhex(line)
            print(b.decode(), end='')
            line = f.readline()


def xxd_dumpline(line: bytes, cols: int = 16, offset: int = 0) -> None:
    # to hex
    hx = ''.join(map(lambda b: '{:02x}'.format(b), line)).ljust(cols * 2)
    # group each two octets
    hx = ' '.join(hx[i : i + 4] for i in range(0, len(hx), 4))

    # ascii preview
    text = ''.join(map(lambda b: chr(b) if b in PRINTABLE else '.', line))
    print('{:08x}: {}  {}'.format(offset, hx, text))


def xxd(fname: str, cols: int = 16, revert: bool = False) -> None:
    """
    fname: file name
    cols: octets per line
    revert: convert hexdump into binary
    """
    if revert:
        return xxd_revert(fname, cols=cols)
    with open(fname, 'rb') as f:
        offset = 0
        line = f.read(cols)
        while line:
            xxd_dumpline(line, cols=cols, offset=offset)
            offset += cols
            line = f.read(cols)


def help(prog: str) -> None:
    print('Syntax: {} [-h] [-r] [-c cols] <file>'.format(prog))
    print('    -h       display this help')
    print('    -r       convert hexdump into binary. Writes directly to stdout.')
    print('    -c cols  format <cols> octets per line. Default 16.')


if __name__ == '__main__':
    if len(argv) == 1:
        help(argv[0])
        exit(0)

    fname = ''
    cols = 16
    revert = False
    i = 1
    while i < len(argv):
        if argv[i] == '-h':
            help(argv[0])
            exit(0)
        if argv[i] == '-r':
            revert = True
            i += 1
        elif argv[i] == '-c':
            cols = int(argv[i + 1])
            i += 2
        else:
            fname = argv[i]
            i += 1

    try:
        xxd(fname, cols=cols, revert=revert)
    except BrokenPipeError:
        pass
    finally:
        stderr.close()  # suppress BrokenPipeError message
