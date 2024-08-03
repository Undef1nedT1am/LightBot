from os import getcwd

import yaml


class Config(object):
    def __init__(self):
        self.runPath = getcwd().replace("\\", "/")
        pass

    def getBotConfig(self):
        with open(f"{self.runPath}/config/config.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data

    def getDevVersion(self):
        with open(f"{self.runPath}/version.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data['devChannel']

    def getBuildTime(self):
        with open(f"{self.runPath}/version.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data['buildTime']
