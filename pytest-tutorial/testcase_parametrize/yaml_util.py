# from PyYAML import yaml
import yaml

class YamlUtil:

    #  将yaml文件传入到此类中
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取yaml文件内容, 对yaml进行反序列化，将yaml文件格式变为dict格式
    def read_yaml(self):
        # 参数： 文件流和加载方式
        # 返回值： 一个value
        # yaml.load(stream, Loader=None)
        with open(self.yaml_file, 'r') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            return value



if __name__ == '__main__':
    yamlUtil = YamlUtil('./test_api.yaml')
    yamlUtil.read_yaml()
