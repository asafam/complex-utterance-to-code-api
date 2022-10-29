from typing import TypeVar, List


T = TypeVar("T")

class DataModel:
    
    data = []
    
    def __init__(self, data) -> None:
        pass
    
    @classmethod
    def set_data(cls, data):
        cls.data = data
        
    @classmethod
    def get_data(cls, T) -> List:
        private_data = [x for x in cls.data if type(x) == T]
        return private_data
    
    @classmethod
    def append(cls, item: T) -> None:
        cls.data.append(item)
        
    