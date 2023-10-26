from functools import wraps
import logging
from logging.handlers import TimedRotatingFileHandler
import os
from asgi_request_id import get_request_id


class MyLogger:
    def process(func):
        @wraps(func)
        def wrapper(self, msg, *args, **kwargs):
            kwargs["extra"] = {"request_id": get_request_id()}
            func(self, msg, *args, **kwargs)

        return wrapper

    def __init__(self, name) -> None:
        self.logger = logging.getLogger(name)
        self.name = name

    def setLevel(self, log_level) -> None:
        self.logger.setLevel(log_level)

    def addHandler(self, handler) -> None:
        self.logger.addHandler(handler)

    @process
    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    @process
    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    @process
    def warn(self, msg, *args, **kwargs):
        self.logger.warn(msg, *args, **kwargs)

    @process
    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    @staticmethod
    def getLogger(name):
        logger = MyLogger(name)
        if not os.path.exists("logs"):
            os.mkdir("logs")
        logger.setLevel(logging.DEBUG)
        file_handler = TimedRotatingFileHandler(
            filename="logs/app.log", when="midnight", backupCount=30
        )
        formatter = logging.Formatter(
            "%(asctime)s %(request_id)s - %(levelname)s: %(message)s"  # noqa
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
