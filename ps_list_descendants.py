#! /usr/bin/env python3
from sys import argv
from typing import Dict, List, Tuple
from subprocess import run, PIPE
"""
    Recursively find all descendants of a parent process. Written by davidhcefx, 2023.8.16

    $ bash -c "ps_list_descendants.py $$; echo; echo subshell:\$$"
Descendants:
PID         PPID        CMD
1737141     4181380     bash -c ps_list_descendants.py 4181380; echo; echo subshell:$$
1737142     1737141     python3 /home/david/bin/ps_list_descendants.py 4181380
1737147     1737142     ps -Af

subshell:1737141
"""

def get_ppid_table() -> Dict[str, List[Tuple[str, str]]]:
    table = dict()
    out = run(['ps', '-Af'], stdout=PIPE, check=True).stdout
    for line in out.decode().strip().split('\n'):
        arr = line.split()
        pid, ppid, cmd = arr[1], arr[2], ' '.join(arr[7:])
        if ppid not in table:
            table[ppid] = [(pid, cmd)]
        else:
            table[ppid].append((pid, cmd))

    return table


def main(pid: str) -> None:
    print('Descendants:')
    print('{:12}{:12}{}'.format('PID', 'PPID', 'CMD'))
    table = get_ppid_table()
    queue = [pid]
    while queue:
        ppid = queue.pop()
        for pid, cmd in table.get(ppid, []):
            print('{:12}{:12}{}'.format(pid, ppid, cmd))
            queue.append(pid)


if __name__ == '__main__':
    if len(argv) > 1:
        main(argv[1])
    else:
        main(input('Enter a PID: '))
