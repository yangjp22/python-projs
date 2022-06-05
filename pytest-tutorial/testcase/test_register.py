import time
import pytest

class TestRegister:

    @pytest.mark.run(order=5)
    def test_01_register(self):
        print("register result")