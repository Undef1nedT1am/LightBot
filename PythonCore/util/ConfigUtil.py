from os import getcwd

import yaml


class Config(object):
    def __init__(self):
        self.runPath = getcwd().replace("\\", "/")

    def getBotConfig(self):
        with open(f"{self.runPath}/config/config.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            del f
            return data

    async def YmlsProcessor(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://github.com/Undef1nedT1am/LightBot/raw/main/PythonCore/config/version.yml") as r:
                version = await r.text()
                async with open("config/version.yml", 'w') as f:
                    f.write(version)
                del r

            async with session.get(
                f"https://github.com/Undef1nedT1am/LightBot/raw/main/PythonCore/config/config.yml") as r:
                config = await r.text()
                async with open("config/config.yml", 'w') as f:
                    f.write(config)
                del r
