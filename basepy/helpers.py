"""Helper methods
"""

from libs.logger import log
import random

DEFAULT_NAMES = [
    "Scott Pilgrim",
    "Ramona Flowers",
    "Stephen Stills",
    "Kim Pine",
    "Young Neil",
    "Knives Chau",
    "Wallace Wells",
    "Gideon Graves",
    "Envy Adams",
]


def greet(name=None, as_a_pirate=False):
    if as_a_pirate:
        log().debug("Pirate mode!")
        return f"Ahoy, {name or _get_random_name()}!"
    return f"Hello, {name or _get_random_name()}!"


def _get_random_name():
    return random.choice(DEFAULT_NAMES)
