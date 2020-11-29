"""Logger
"""

import logging
import logging.config


logging.config.fileConfig("logging.ini")


def log():
    return logging.getLogger("defaultLogger")
