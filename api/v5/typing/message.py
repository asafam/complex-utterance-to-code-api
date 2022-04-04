from abc import abstractclassmethod
from __future__ import annotations
from resolveable import Resolveable
from typing.generic import Contact, DateTime, Location, Entity
from typing import Callable, Optional


class MessageContent(Entity, Resolveable):
    pass


class Message(Entity):
    date_time: DateTime
    sender: Contact
    content: MessageContent

    @abstractclassmethod
    def get_predicate(
        Message,
        date_time: Optional[DateTime] = None,
        sender: Optional[Contact] = None,
        content: Optional[MessageContent] = None,
    ) -> Callable[[Message], bool]:
        raise NotImplementedError
