#!/usr/bin/env python3
"""Constroe e distribui a documentação sphinx."""

import argparse
import os


def main():
    """Executa o módulo."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--construir', action='store_true', default=False, dest='construir')
    parser.add_argument('--distribuir', action='store_true', default=False, dest='distribuir')
    parser.add_argument('--port', type=int, dest='port', default=9000)
    args = parser.parse_args()

    cmd = ''
    if args.construir:
        cmd = 'make clean;make html;make latexpdf;make html'

    if args.distribuir:
        cmd = f'make clean;make html;make latexpdf;make html;livereload ./build/html -p {args.port}'

    if cmd:
        os.system(cmd)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
