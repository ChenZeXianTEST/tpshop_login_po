import os

import yaml


class ReadYaml():

    def __init__(self, filename):
        self.local_run = filename
        self.filename = os.getcwd()+os.sep+"data"+os.sep+filename

    def read_yaml_data(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return yaml.load(f)

    def read_yaml_data_local_run(self):
        with open("../data/"+self.local_run, "r", encoding="utf-8") as f:
            return yaml.load(f)


if __name__ == '__main__':
    datas = ReadYaml("data_login.yaml").read_yaml_data_local_run().values()
    print(datas)
    list1 = []
    for data in datas:
        list1.append((data.get("username"), data.get("password"), data.get("number")))

    for i in list1:
        print(i)
