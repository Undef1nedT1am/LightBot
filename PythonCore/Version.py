import yaml
import aiofiles

class Version:
    def __init__(self):
        self.versionPath = "config/version.yml"

    async def getDevVersion(self):
        async with aiofiles.open(f"{self.versionPath}", "r") as f:
            data = await yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data['devChannel']

    async def getBuildTime(self):
        async with aiofiles.open(f"{self.versionPath}", "r") as f:
            data = await yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data['buildTime']
