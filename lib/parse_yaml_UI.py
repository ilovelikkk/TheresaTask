import os

import yaml


def parseyaml():
    # 当前脚本路径的父类
    basepath = os.path.dirname(os.path.dirname(__file__))
    # yaml_path=basepath+"\\PageElement"
    yaml_path = basepath + "\\data"
    pageElements = {}
    # 遍历读取yaml文件

    for fpath, dirname, fnames in os.walk(yaml_path):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath, name)
            print(yaml_file_path)
            # 排除一些非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    # 返回字典内容
    # for i in pageElements[pagename]['locators']:
    #   print(i)
    return pageElements