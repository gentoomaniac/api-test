#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import sys
import http

import click
import requests


log = logging.getLogger(__name__)

API_ENDPOINT = "http://127.0.0.1:8000/example_2.json"


def _configure_logging(verbosity):
    loglevel = max(3 - verbosity, 0) * 10
    logging.basicConfig(
        level=loglevel,
        format="[%(asctime)s] %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


@click.command()
@click.option("-v", "--verbosity", help="Verbosity", default=0, count=True)
def cli(verbosity: int):
    """main program"""
    _configure_logging(verbosity)

    log.info("I am an informational log entry in the sample script.")

    try:
        response = requests.request(
            "GET",
            url=API_ENDPOINT,
            headers={"USERNAME": "foo", "PASSWORD": "bar"},
            timeout=10,
        )

        log.info(response.status_code)
        if response.status_code != 200:
            log.error("not 200")

        data = response.json()

        print(json.dumps(data["quiz"]["sport"], indent=2, sort_keys=True))

        response = {
            "title": "fizzbuzz",
            "data": "kjdfkjnwerkgnwkjtnhwirhtuwrtniuwitgnjiru",
        }

        resp = requests.request(
            "POST",
            url="http://127.0.0.1:8000",
            headers={},
            data=json.dumps(response),
            timeout=10,
        )

        if resp.status_code != 201:
            log.error(resp.status_code)

    except Exception as e:
        log.error(e)

    return 0


if __name__ == "__main__":
    # pylint: disable=E1120
    sys.exit(cli())
