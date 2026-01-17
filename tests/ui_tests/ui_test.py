import pytest

@pytest.fixture
def common_fixture():
    return 100

def ui_test(ui_fixture, common_fixture):
    pass
