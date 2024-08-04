from os import getcwd
import aiohttp
import yaml
import aiofiles
class Config(object):
    def __init__(self):
        self.runPath = getcwd().replace("\\", "/")

    async def getBotConfig(self):
        async with (aiofiles.open(f"{self.runPath}/config/config.yml", "r") as f):
            data = await f.read()
            data_yaml = yaml.safe_load(data)
            del f
            return data_yaml

    async def YmlsProcessor(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://github.com/Undef1nedT1am/LightBot/raw/main/PythonCore/config/version.yml") as r:
                version = await r.text()
                async with aiofiles.open("config/version.yml", 'w') as f:
                    await f.write(version)
                del r

            async with session.get(
                f"https://github.com/Undef1nedT1am/LightBot/raw/main/PythonCore/config/config.yml") as r:
                config = await r.text()
                async with aiofiles.open("config/config.yml", 'w') as f:
                    await f.write(config)
                del r
