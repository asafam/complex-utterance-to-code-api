from abc import abstractclassmethod
from typing import Iterable, Union, Optional
from api.v6.entities.resolvable import Resolvable
from entities.generic import Entity
from typing.apps import App


class AppsCommand(Resolvable):
    
    @abstractclassmethod
    def open(
        app: Optional[App] = None,
    ) -> bool:
        raise NotImplementedError

