import pytest
import random

@pytest.fixture
def overridable_fixture():
    return random.randint(1, 100)