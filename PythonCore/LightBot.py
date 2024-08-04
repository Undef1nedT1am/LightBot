import asyncio

from PythonCore.util.ConfigUtil import Config
from PythonCore.util.Network import Network, HttpEventNetwork
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
    configs = await config.getBotConfig()
    if configs['program']['disableRuntimeWarnings']:
        import warnings
        warnings.filterwarnings("ignore", category=RuntimeWarning)
    # Program
    await logger.info("LightBot starting...")
    dev_version = await version.getDevVersion()
    build_time = await version.getBuildTime()
    if configs['program']['checkUpdate']:
        await logger.info("Checking updates...")
        await config.YmlsProcessor()
        await logger.warn(
            "Because the version and config file are downloaded from github, so it often timed out.You need a VPN.")
        await logger.success(f"Checked updates and replaced the file. Now the version:{dev_version}")


        await chat.sendMsg("group", 194167989,
                       f"LightBot Dev Version v{dev_version} by Yurnu launch successfully.\rUsed time:{timer.end()}\rBuild time: {build_time}")

if __name__ == "__main__":

    asyncio.run(main())
    network = Network()
    if network.protocol == "http":
        eventServer = HttpEventNetwork("127.0.0.1:3001")#configs['bot']['httpEventHost'])
        eventServer.Server()
