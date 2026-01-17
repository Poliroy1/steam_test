import pytest

@pytest.fixture
def common_fixture():
    return 100

def ui_test(common_fixture):
    pass
