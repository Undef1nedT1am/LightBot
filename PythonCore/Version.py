from os import getcwd, path as osp, mkdir

import yaml


#


class Version:
    def __init__(self):
        self.versionPath = "config/version.yml"
    def getDevVersion(self):
        with open(f"{self.versionPath}", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data['devChannel']

    def getBuildTime(self):
        with open(f"{self.versionPath}", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data['buildTime']

if __name__ == "__main__":
    version = Version()
