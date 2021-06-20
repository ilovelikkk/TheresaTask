import os

import yaml


def parseyaml(type):
    basepath = os.path.dirname(os.path.dirname(__file__))
    # yaml_path=basepath+"\\PageElement"
    yaml_path = basepath + "\\data\\"+type
    pageElements = {}

    for fpath, dirname, fnames in os.walk(yaml_path):
        for name in fnames:
            yaml_file_path = os.path.join(fpath, name)
            print(yaml_file_path)
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path, 'r', encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)

    # for i in pageElements[pagename]['locators']:
    #   print(i)
    return pageElements
