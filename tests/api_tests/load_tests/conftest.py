import pytest
import random

@pytest.fixture
def api_fixture():
    return random.randint(1, 100)