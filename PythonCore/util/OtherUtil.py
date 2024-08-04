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
        self.logConfig = self.config.getBotConfig()['log']

    def log(self, log_type, message):
        color_codes = {
            'INFO': '\033[0m',
            'SUCCESS': '\033[92m',
            'WARN': '\033[93m',
            'ERROR': '\033[91m'
        }
        reset_color = '\033[0m'
        now = datetime.now()
        logTimePart = f" - {now.hour} : {now.minute} : {now.second}" if self.logConfig['printTime'] else ""
        formatted_message = f"{color_codes[log_type.upper()]}[{log_type.upper()}{logTimePart}] {message}{reset_color}"
        print(formatted_message)

    def info(self, message):
        self.log('INFO', message)

    def success(self, message):
        self.log('SUCCESS', message)

    def warn(self, message):
        self.log('WARN', message)

    def error(self, message):
        self.log('ERROR', message)
