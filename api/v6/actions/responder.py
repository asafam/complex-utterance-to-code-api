from abc import abstractclassmethod
from typing import Iterable, Union
from api.v6.entities.resolvable import Resolvable
from entities.generic import Entity


class Responder(Resolvable):
    
    @abstractclassmethod
    def respond(cls, response: Union[Iterable[Entity], Entity]):
        raise NotImplementedError
