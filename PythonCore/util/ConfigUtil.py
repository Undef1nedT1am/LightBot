import asyncio
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
            try:
                version_response, config_response = await asyncio.gather(
                    session.get(f"https://github.com/Undef1nedT1am/LightBot/raw/main/PythonCore/config/version.yml"),
                    session.get(f"https://github.com/Undef1nedT1am/LightBot/raw/main/PythonCore/config/config.yml")
                )
                if version_response.status != 200 or config_response.status != 200:
                    print("[INFO] Could not update. Check your network")
                # 读取响应内容并写入本地文件
                version_text = await version_response.text()
                with open("config/version.yml", 'w') as f:
                    f.write(version_text)

                config_text = await config_response.text()
                with open("config/config.yml", 'w') as f:
                    f.write(config_text)
            except:
                pass


