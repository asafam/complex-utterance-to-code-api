from __future__ import annotations
from abc import abstractmethod


class Entity:
    
    @abstractmethod
    def call(self, funcName: str, params: dict[str, str]) -> any:
        raise NotImplementedError("Subclass should implement this method")
    
    @abstractmethod
    def getattr(self, name: str) -> any:
        raise NotImplementedError("Subclass should implement this method")
    
    @abstractmethod
    def compare(self, entity: Entity) -> bool:
        raise NotImplementedError("Subclass should implement this method")
    