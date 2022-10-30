from abc import abstractclassmethod
from typing import Iterable, Union
from entities.resolvable import Resolvable
from entities.generic import Entity


class Responder(Resolvable):
    
    @classmethod
    def respond(cls, response: Union[Iterable[Entity], Entity]):
        pass
