import pytest

@pytest.fixture(scope="function")
def myFixture():
    print("I am in the fixture of conftest.py")
