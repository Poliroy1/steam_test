import random
import pytest


@pytest.fixture
def ui_fixture():
    return random.randint(1,1000)

