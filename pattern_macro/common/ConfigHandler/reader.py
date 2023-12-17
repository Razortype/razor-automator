from abc import ABC, abstractmethod
from attrdict import AttrDict
import json
# ToDo:
# import attrdict
# return attrdict dot seperated json config value

import os

class IDataReader(ABC):

    @abstractmethod
    def get_json(self):
        pass

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod 
    def read_json(self):
        pass

# -------------

class DataReader(IDataReader):

    @classmethod
    def get_json(cls, path:str) -> str:
        json_obj = cls.read_json(path)
        return json_obj

    @classmethod
    def get_config(cls, path:str) -> AttrDict:
        raw_json = cls.get_json(path)
        return AttrDict(raw_json)
    
    @staticmethod
    def read_json(path:str) -> str:
        with open(path, "r") as json_file:
            data = json.loads(json_file.read())
        return data

# ------------- VARS