#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

import click

from python_template import foo

log = logging.getLogger(__name__)


def _configure_logging(verbosity):
    loglevel = max(3 - verbosity, 0) * 10
    logging.basicConfig(level=loglevel, format='[%(asctime)s] %(name)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


@click.group()
@click.option('-v', '--verbosity', help='Verbosity', default=0, count=True)
def cli(verbosity: int):
    """ main program
    """
    _configure_logging(verbosity)

    log.info('I am an informational log entry in the sample script.')
    return 0


@cli.command(name='foo')
def foobar():
    log.debug("foo")
    print(foo.bar())

if __name__ == '__main__':
    # pylint: disable=E1120
    sys.exit(cli())
