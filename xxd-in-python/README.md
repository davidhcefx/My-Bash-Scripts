# Simple xxd in Python

This is a Python tool to mimic the [`xxd(1)`](https://linux.die.net/man/1/xxd) created by Juergen Weigert:

> xxd - make a hexdump or do the reverse.

The supported options are:

- -r: convert hexdump into binary. Writes directly to stdout.

- -c cols: format <cols> octets per line. Default 16.


## Example

```sh
$ ./xxd.py xxd.py | head
00000000: 2321 202f 7573 722f 6269 6e2f 656e 7620  #! /usr/bin/env
00000010: 7079 7468 6f6e 330a 2320 546f 6f6c 2074  python3.# Tool t
00000020: 6f20 6d69 6d69 6320 7878 6428 3129 2e20  o mimic xxd(1).
00000030: 5772 6974 7465 6e20 6279 2064 6176 6964  Written by david
00000040: 6863 6566 782c 2032 3032 352e 342e 390a  hcefx, 2025.4.9.
00000050: 6672 6f6d 2073 7973 2069 6d70 6f72 7420  from sys import
00000060: 6172 6776 2c20 7374 6465 7272 0a66 726f  argv, stderr.fro
00000070: 6d20 7374 7269 6e67 2069 6d70 6f72 7420  m string import
00000080: 6173 6369 695f 6c65 7474 6572 732c 2064  ascii_letters, d
00000090: 6967 6974 732c 2070 756e 6374 7561 7469  igits, punctuati
```
