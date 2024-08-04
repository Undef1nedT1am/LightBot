import asyncio

from PythonCore.util.ConfigUtil import Config
from util.QQ.ChatUtil import Chat
from util.OtherUtil import Timer, Logger
from Version import Version
from os import path as osp, mkdir


async def main():
    # ini
    timer = Timer()
    timer.start()
    if not osp.exists("config"):
        mkdir("config")
    config = Config()
    version = Version()
    chat = Chat()
    logger = Logger()

    # Program
    logger.info("LightBot starting...")
    logger.info("Checking updates...")
    logger.warn("Because the version and config file are downloaded from github, so it often timed out.You need a VPN.")
    await config.YmlsProcessor()
    logger.success(f"Checked updates and replaced the file. Now the version:{version.getDevVersion()}")
    await chat.sendMsg("group", 194167989,
                       f"LightBot Dev Version v{version.getDevVersion()} by Yurnu launch successfully.\rUsed time:{timer.end()}\rBuild time: {version.getBuildTime()}")


if __name__ == "__main__":
    asyncio.run(main())
