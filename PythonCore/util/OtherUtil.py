import time
from datetime import datetime
from PythonCore.util.ConfigUtil import Config


class Timer:
    def __init__(self):
        self.startTime = 0
        self.endTime = 0

    def start(self):
        self.startTime, self.endTime = 0, 0
        self.startTime = time.time()

    def end(self) -> float:
        self.endTime = time.time()
        return self.endTime - self.startTime


class Logger:
    def __init__(self):
        self.config = Config()
        self.logConfig = {}

    async def log(self, log_type, message):
        color_codes = {
            'INFO': '\033[0m',
            'SUCCESS': '\033[92m',
            'WARN': '\033[93m',
            'ERROR': '\033[91m'
        }
        reset_color = '\033[0m'
        now = datetime.now()
        self.logConfig = await self.config.getBotConfig()

        logTimePart = f" - {now.hour} : {now.minute} : {now.second}" if self.logConfig['log']['printTime'] else ""
        formatted_message = f"{color_codes[log_type.upper()]}[{log_type.upper()}{logTimePart}] {message}{reset_color}"
        print(formatted_message)

    async def info(self, message):
        await self.log('INFO', message)

    async def success(self, message):
        await self.log('SUCCESS', message)

    async def warn(self, message):
        await self.log('WARN', message)

    async def error(self, message):
        await self.log('ERROR', message)
