from __future__ import annotations
from abc import abstractclassmethod
from typing import TypeVar, Type, Generic


T = TypeVar("T", bound="Resolveable")


class Resolveable(Generic[T]):
    """
    Markup class
    """

    @abstractclassmethod
    def resolve_from_text(cls: T, text: str) -> T:
        raise NotImplementedError
