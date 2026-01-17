import random

import pytest

@pytest.fixture
def api_fixture():
    return random.randint(1, 250)