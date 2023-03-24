import sys, os
import datetime
import logging
from logging import StreamHandler, Formatter
'''
Класс, включащий в себя все конфигурации logging
для дальнейшего логирования программы.
'''
class Logging:
    def __init__(self) -> None:
        logpath = r'logs'
        if not os.path.exists(logpath):
            os.makedirs(logpath)

    def _logger(self, classself) -> logging.getLogger:
        self.logger = None
        if None == self.logger:
            self.logger = logging.getLogger(str(classself))
            self.logger.setLevel(logging.DEBUG)
            self.logger.propagate = False
            self.logger.propagate = False
            self.fhandler = logging.FileHandler('logs/latest.log')
            self.fhandler.setFormatter(Formatter(fmt=f'[%(asctime)s: %(levelname)s] %(message)s ({classself})'))
            self.logger.addHandler(self.fhandler)

            return self.logger
        