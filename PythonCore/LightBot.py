import asyncio

from PythonCore import UvicornServer
from PythonCore.util.ConfigUtil import Config
from PythonCore.util.Network import Network
from util.QQ.ChatUtil import Chat
from util.OtherUtil import Timer, Logger
from Version import Version
from os import path as osp, mkdir


async def main():
    # ini
    config = Config()
    configs = config.noAsyncGetBotConfig()
    timer = Timer()
    version = Version()
    logger = Logger()
    timer.start()
    if not osp.exists("config"):
        mkdir("config")

    dev_version = await version.getDevVersion()
    build_time = await version.getBuildTime()
    if configs['program']['disableRuntimeWarnings']:
        import warnings
        warnings.filterwarnings("ignore", category=RuntimeWarning)
    # Program
    await logger.info("LightBot starting...")

    if configs['program']['checkUpdate']:
        await logger.info("Checking updates...")
        await config.YmlsProcessor()
        await logger.warn(
            "Because the version and config file are downloaded from github, so it often timed out.You need a VPN.")
        await logger.success(f"Checked updates and replaced the file. Now the version:{dev_version}")
    chat = Chat()

    await chat.sendMsg("group", 194167989,
                       f"LightBot Dev Version v{dev_version} by Yurnu launch successfully.\rUsed time:{timer.end()}\rBuild time: {build_time}")


if __name__ == "__main__":
    network = Network()
    asyncio.run(main())

    if network.protocol == "http":
        print(5)
        UvicornServer.start()
