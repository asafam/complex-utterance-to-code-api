from typing import Iterable, Union
from typing.generic import Entity


def default_responder(response: Union[Iterable[Entity], Entity]):
    raise NotImplementedError
