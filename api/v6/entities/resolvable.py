from __future__ import annotations
from abc import abstractclassmethod, abstractmethod
from typing import TypeVar, Generic, Optional, Union, List
from exceptions.exceptions import exception_handler
from providers.data_model import DataModel


T = TypeVar("T", bound="Resolvable")


class Resolvable(Generic[T]):
    """
    Markup class
    """

    # @exception_handler
    @classmethod
    def resolve_from_text(
        T, text: str, recovered_text: Optional[str] = None
    ) -> T:
        data = DataModel.get_data(T)
        if data is None:
            raise NotImplementedError()

        items = [x for x in data if x.data.get("text") == text]

        if len(items) == 0:
            raise ValueError()
        else:
            result = items[0]
            return result
        
    @classmethod
    def resolve_many_from_text(
        T, text: str, recovered_text: Optional[str] = None
    ) -> List[T]:
        data = DataModel.get_data(T)
        if data is None:
            raise NotImplementedError()

        items = [x for x in data if x.data.get("text") == text]

        if len(items) == 0:
            raise ValueError()
        else:
            result = items
            return result

    @exception_handler
    @abstractclassmethod
    def resolve_from_entity(
        T,
        entity: Union[T, List[T]],
        recovered_entity: Optional[Union[T, List[T]]] = None,
    ) -> T:
        raise NotImplementedError
