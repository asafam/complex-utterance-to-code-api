from abc import abstractclassmethod
from entities.entity import Entity


class Task:
    
    @abstractclassmethod
    def find(cls, query: dict[str, str]) -> list[Entity]:
        pass
    
    @abstractclassmethod
    def findOne(cls, query: dict[str, str]) -> Entity:
        pass
    
    @abstractclassmethod
    def create (cls, params: dict[str, str]) -> Entity:
        pass
    
    @abstractclassmethod
    def update(cls, query: dict[str, str], params: dict[str, str]) -> int:
        pass
        