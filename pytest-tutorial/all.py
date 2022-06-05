import pytest
import os

if __name__ == '__main__':
    # pytest.main(['-m=smoke or username'])
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')
    