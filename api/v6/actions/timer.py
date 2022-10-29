from abc import abstractclassmethod
from typing import Iterable, Union, Optional
from api.v6.entities.resolvable import Resolvable
from entities.entity import Entity
from entities.timer import Timer


class TimerCommand(Resolvable):
    
    @abstractclassmethod
    def pause(
        cls,
        timer: Optional[Timer] = None,
    ) -> bool:
        raise NotImplementedError

    @abstractclassmethod    
    def restart(
        cls,
        timer: Optional[Timer] = None,
    ) -> bool:
        raise NotImplementedError

    @abstractclassmethod
    def stop(
        cls,
        timer: Optional[Timer] = None,
    ) -> bool:
        raise NotImplementedError
