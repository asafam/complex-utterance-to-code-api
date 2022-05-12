from abc import abstractclassmethod
from typing import Iterable, Union, Optional
from api.v5.exceptions.resolvable import Resolvable
from typing.generic import Contact, DateTime, Entity
from typing.message import Message, Content


class MessagesCommand(Resolvable):
    @abstractclassmethod
    def send_message(
        cls,
        recipient: Optional[Contact] = None,
        exact_content: Optional[Content] = None,
    ) -> Message:
        raise NotImplementedError
