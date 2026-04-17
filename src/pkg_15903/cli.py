#!/usr/bin/env python

"""
Purpose: run some test package
"""

import click

from pkg_15903 import ClsRequests, ClsValidate, __version__


@click.command()
@click.option('--url', required=True, type=ClsValidate.chk_url)
@click.version_option(version=__version__)
def main(url):
    print('Starting Requests...')

    req = ClsRequests()
    req.checklinks(url=url)


if __name__ == '__main__':  # pragma: no cover
    main()
