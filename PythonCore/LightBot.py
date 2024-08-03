import asyncio
from util.QQ.ChatUtil import Chat
from util.OtherUtil import Timer
from util.ConfigUtil import Config


async def main():
    config = Config()
    timer = Timer()
    timer.start()
    chat = Chat()
    await chat.sendMsg("group", 194167989,
                       f"LightBot Dev Version v{config.getDevVersion()} by Yurnu launch successfully.\rUsed time:{timer.end()}\rBuild time: {config.getBuildTime()}")


if __name__ == "__main__":
    asyncio.run(main())
