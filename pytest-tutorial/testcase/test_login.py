import pytest
import time

# @pytest.fixture(scope="function", params=[{'a': 10}, {'a':15}, {'a': 20}])
# def fixture(request):
#     # print(request)
#     print("I am using fixture")
#     # return request.param
#     yield request.param
#     print("I am using later fixture")
#     # return request.param


class TestLogin:

    def setup_class(self):
        print("I am in setup class")
    
    def setup(self):
        print("I am in setup")

    # age = 20
    # @pytest.mark.run(order=2)
    # @pytest.mark.smoke
    def test_01_login(self, myFixture):
        print("I am in fixture of test 01")
        print("test 01")

    # @pytest.mark.run(order=1)
    # @pytest.mark.username
    # @pytest.mark.skip(reason="one")
    def test_02_login(self):
        # assert 1 == 2
        print("test 02") 

    # @pytest.mark.run(order=2)
    # @pytest.mark.skipif(age > 18, reason="adult")
    # def test_03_login(self):
    #     # assert 1 == 2
    #     print("test 03") 

    # def test_04_login(self):
    #     # assert 2 == 3
    #     print("test 04") 

    # def test_05_login(self):
    #     print("test 05")

    def teardown(self):
        print("I am in teardown")

    def teardown_class(self):
        print("I am in teardown class")
# if __name__ == '__main__':
#     pytest.main()