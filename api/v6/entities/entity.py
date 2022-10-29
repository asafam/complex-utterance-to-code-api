
from __future__ import annotations
from abc import abstractclassmethod, abstractmethod


class Entity:
    
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.data = kwargs
        
    @abstractmethod
    def __gt__(self, other) -> bool:
        raise NotImplementedError()