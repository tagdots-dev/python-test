#!/usr/bin/env python

"""
Purpose: run some test package
"""

import click

from pkg_15903 import __version__
from pkg_15903.core.cls_requests import ClsRequests
from pkg_15903.utils.validation import ClsValidate


@click.command()
@click.option('--url', required=True, type=ClsValidate.chk_url)
@click.version_option(version=__version__)
def main(url):
    print('Starting Requests...')

    start = ClsRequests()
    start.checklinks(url=url)


if __name__ == '__main__':  # pragma: no cover
    main()
