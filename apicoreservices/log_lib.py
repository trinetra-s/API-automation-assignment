import logging
import os
import sys

class Log():

    @classmethod
    def log_config(cls, userLevel=logging.INFO):
        logger = logging.getLogger(__name__)
        logger.setLevel(level=userLevel)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        file_handler = logging.FileHandler(os.path.abspath(os.path.join('apitestlogs','api.log')))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info(msg='---------------------------------------------------------')
        return logger


