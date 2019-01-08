#!/usr/bin/env python3
"""Executa compila a documentação e distribui localmente utilizando livereload."""

import argparse
import os


def main():
    """Main."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='ip do host')
    parser.add_argument('--port', default=9000, type=int, help='porta do servidor, default 9000')
    args = parser.parse_args()

    cmd = f'make clean;make html;make latexpdf;make html;'
    cmd += f'livereload build/html/ --host {args.host} --port {args.port}'
    os.system(cmd)


if __name__ == '__main__':
    main()
