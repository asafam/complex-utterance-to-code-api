from __future__ import annotations
from abc import abstractclassmethod
from resolveable import Resolveable


class Entity():
    pass

class Contact(Entity, Resolveable):
    pass


class DateTime(Entity, Resolveable):
    pass
    
    
class Location(Entity, Resolveable):
    pass