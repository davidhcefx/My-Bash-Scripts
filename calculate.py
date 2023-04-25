#! /usr/bin/env python3
# Just a simple CLI math calculator. Written by davidhcefx, 2023.4.25.
#
from sys import argv
from os.path import basename
try:
    # list of additional modules that might be helpful
    import math         # noqa:F401
    import numpy as np  # noqa:F401
except ModuleNotFoundError:
    pass


def calc(expr: str) -> str:
    """Evaluate expr and return the result."""
    return str(eval(expr))


if __name__ == '__main__':
    if len(argv) == 1:
        print('Syntax: {} "math-expression" ...'.format(basename(argv[0])))
        raise SystemExit()

    for r in map(calc, argv[1:]):
        print(r)
