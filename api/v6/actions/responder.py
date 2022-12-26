from abc import abstractclassmethod
from typing import Iterable, Union
from entities.resolvable import Resolvable
from entities.generic import Entity
from providers.data_model import DataModel


class Responder(Resolvable):
    
    @classmethod
    def respond(cls, response: Union[Iterable[Entity], Entity]):
        data_model = DataModel()
        data_model.append_output_data(response)
