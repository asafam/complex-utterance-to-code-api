from abc import abstractclassmethod
from typing import Iterable, Union, Optional
from api.v6.entities.resolvable import Resolvable
from entities.generic import Entity
from entities.app import App


class Apps(Resolvable):
    
    @abstractclassmethod
    def open(
        cls,
        app: Optional[App] = None,
    ) -> bool:
        raise NotImplementedError

