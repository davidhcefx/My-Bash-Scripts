#! /usr/bin/python3
from sys import argv
from os.path import basename


def color256(code: str) -> int:
    rgb = [int(code[i:i+2], 16) for i in range(0, len(code), 2)]
    ruler = [0, 95, 135, 175, 215, 255]  # the scale used by 256 color
    ret_idx = 0
    for value in rgb:
        # find closest match on ruler
        for i, _ in enumerate(ruler):
            if ruler[i] <= value <= ruler[i + 1]:
                idx = i if (value - ruler[i] < ruler[i + 1] - value) else i + 1
                break
        ret_idx = ret_idx * len(ruler) + idx

    return ret_idx + 16  # (0, 0, 0) starts from 16


def help_exit():
    raise SystemExit('Example: {} a6e22e'.format(basename(argv[0])))


if __name__ == '__main__':
    if len(argv) == 1:
        help_exit()
    else:
        code = argv[1].strip('#')
        if len(code) != 6:
            help_exit()

        color = '\x1b[38;5;{}m'.format(color256(code))
        reset = '\x1b[0m'
        head = color + '▁▂▃▄▅▆▇█' + '█' * 10 + reset
        tail = color + '█' * 10 + '█▇▆▅▄▃▂▁' + reset

        print(f'{head} {color}#{code}{reset} looks like this {tail}')
