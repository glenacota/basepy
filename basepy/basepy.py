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

    if names:
        list_of_names = names.split(",")
        [click.echo(greet(name, as_a_pirate)) for name in list_of_names]
    else:
        click.echo(greet(as_a_pirate=as_a_pirate))
    log().debug("All is good!")
