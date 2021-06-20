import os
import yaml


# This is to import the yaml file to dict data


def parseyaml(type):
    basepath = os.path.dirname(os.path.dirname(__file__))
    # yaml_path=basepath+"\\PageElement"
    yaml_path = basepath + "\\data\\" + type  # type can be 'UI' or API, control in before_feature in environment.py
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
