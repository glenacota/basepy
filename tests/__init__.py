import os
import sys
import logging
import pytest

project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
api_path = os.path.join(project_path, os.path.basename(project_path))
sys.path.append(api_path)


@pytest.fixture()
def initlog():
    logger = logging.getLogger("defaultLogger")
    logger.propagate = True
