import logging

import logging
from typing import NewType

LVL = NewType("LVL", int)

class BaseAuxilaryLogger:

    DEBUG=10
    INFO=20
    WARN=30
    ERROR=40
    CRITICAL=50
    
    def __init__(self,
                 name:str) -> None:
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.info(f'Logger Created : "{name}"')

    def log(self, msg:str, lvl:LVL):
        '''
        options: [ DEBUG, INFO, WARN, ERROR, CRITICAL ]
        usage: self.logger.WARN
        '''
        self.logger.log(msg=msg, level=lvl)

    def start_conf(self) -> None:
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

    def debug(self, message):
        self.log(message, lvl=self.DEBUG)

    def info(self, message):
        self.log(message, lvl=self.INFO)

    def warn(self, message):
        self.log(message, lvl=self.WARN)

    def error(self, message):
        self.log(message, lvl=self.ERROR)

    def critical(self, message):
        self.log(message, lvl=self.CRITICAL)

class ConsoleLogger(BaseAuxilaryLogger):
    
    def __init__(self, 
                 name: str) -> None:
        super().__init__(name)

    def start_conf(self) -> None:
        super().start_conf()
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(levelname)-8s %(message)s',)
        
class FileLogger(BaseAuxilaryLogger):
    
    def __init__(self, 
                 name: str,
                 log_path:str) -> None:
        super().__init__(name)
        self.log_path = log_path

    def start_conf(self) -> None:
        
        super().start_conf()        
        logging.basicConfig(
            level=logging.DEBUG,
            filename=self.log_path,
            filemode='a',
            format='%(asctime)s %(levelname)-8s %(message)s',
            datefmt='%y-%m-%d %H:%M:%S')


def generate_logger(log_type:str, logger_name:str=__name__, log_path:str=None):
    
        match log_type:
            case "CONSOLE":
                logger = ConsoleLogger(
                    name=logger_name)
            case "FILE":
                logger = FileLogger(
                    name=logger_name,
                    log_path=log_path
                )
            case _:
                raise RuntimeError(f'Not valid "LOG_TYPE" : {log_type}')
        
        logger.start_conf()
        return logger