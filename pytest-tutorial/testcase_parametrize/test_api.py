import pytest
import requests
# from testcase_parametrize.yaml_util import YamlUtil
from .yaml_util import YamlUtil


class TestApi:

    # def test_login(self):
    #     url = 'https://api.weixin.qq.com/cgi-bin/token'
    #     params = {
    #         'grant_type': 'client_credential',
    #         'appid': 'wx6b11b3efd1cdc290',
    #         'secret': '106a9c6157c4db5f6029918738f9529d'
    #     }
    #     res = requests.get(url, params)
    #     print(res.text)


    @pytest.mark.parametrize('args', argvalues = YamlUtil('./test_api.yaml').read_yaml())
    # def test_login(self, args, param):
    def test_login(self, args):
        url = args['requests']['url']
        params = args['requests']['params']
        res = requests.get(url, params)
        # print(res.text)

        # 断言

if __name__ == '__main__':
    test = TestApi()
    test.test_login()