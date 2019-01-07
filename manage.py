#!/usr/bin/env python3
"""Constroe e distribui a documentação sphinx do projeto."""

import argparse
import logging
import os

logger = logging.getLogger('manage')


def configurar_logger():
    """Configura o logging."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] - %(message)s',
        datefmt=r'%d\%b\%Y %H:%M:%S'
    )


def main():
    """Executa o módulo."""
    configurar_logger()

    host = '0.0.0.0'

    parser = argparse.ArgumentParser()
    parser.add_argument('--executar', action='store_const', const='executar', dest='opção')
    parser.add_argument('--construir', action='store_const', const='construir', dest='opção')
    parser.add_argument('--distribuir', action='store_const', const='distribuir', dest='opção')
    parser.add_argument('--port', type=int, dest='port', default=9000)
    args = parser.parse_args()

    if args.opção:
        if args.opção == 'executar':
            logger.info('Executando servidor de documentação...')
            os.system(f'sphinx-autobuild source/ build/ --host {host} -p {args.port}')

        if args.opção == 'construir':
            logger.info('Construindo documentação...')
            os.system(f'make clean;make html;make latexpdf;make html')

        if args.opção == 'distribuir':
            logger.info('Distribuindo documentação...')
            cmd = f'make clean;make html;make latexpdf;make html;livereload ./build/html '
            cmd += f'--host {host} -p {args.port}'
            os.system(cmd)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
