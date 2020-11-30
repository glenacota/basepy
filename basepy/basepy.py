"""Dummy module
"""

import click
from libs.logger import log


@click.group()
def run():
    """ A simple CLI """
    pass


@run.command()
@click.option("--names", "-n", help="Comma-separated list of names [default: a Scott Pilgrim's character]")
@click.option("--as-a-pirate", "-p", count=True, help="Greet as a pirate")
def greet(names, as_a_pirate):
    """ Greet someone """
    from helpers import greet

    list_of_names = _parse_arg(names)
    [click.echo(greet(name, as_a_pirate)) for name in list_of_names]
    log().debug("All is good!")


def _parse_arg(names):
    return names.split(",") if names else [None]
