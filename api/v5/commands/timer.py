from typing import Iterable, Union, Optional
from typing.generic import Entity
from typing.timer import Timer


def pause(
    timer: Optional[Timer] = None,
) -> bool:
    raise NotImplementedError


def restart(
    timer: Optional[Timer] = None,
) -> bool:
    raise NotImplementedError


def stop(
    timer: Optional[Timer] = None,
) -> bool:
    raise NotImplementedError
