import yaml
import aiofiles

class Version:
    def __init__(self):
        self.versionPath = "config/version.yml"

    async def getDevVersion(self):
        async with aiofiles.open(f"{self.versionPath}", "r") as f:
            data = await f.read()
            data_yaml = yaml.safe_load(data)
            del f
            return data_yaml['devChannel']

    async def getBuildTime(self):
        async with (aiofiles.open(f"{self.versionPath}", "r") as f):
            data = await f.read()
            data_yaml = yaml.safe_load(data)
            del f
            return data_yaml['buildTime']
