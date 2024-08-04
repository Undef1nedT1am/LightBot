import asyncio

from PythonCore.util.ConfigUtil import Config
from util.QQ.ChatUtil import Chat
from util.OtherUtil import Timer
from Version import Version
from os import path as osp, mkdir

async def main():
    if not osp.exists("config"):
        mkdir("config")
    config = Config()
    version = Version()
    timer = Timer()
    timer.start()
    chat = Chat()
    await config.YmlsProcessor()
    await chat.sendMsg("group", 194167989,
                       f"LightBot Dev Version v{version.getDevVersion()} by Yurnu launch successfully.\rUsed time:{timer.end()}\rBuild time: {version.getBuildTime()}")


if __name__ == "__main__":
    asyncio.run(main())
