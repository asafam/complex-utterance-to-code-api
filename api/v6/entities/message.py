from abc import abstractclassmethod
from __future__ import annotations
from resolvable import Resolvable
from entities.generic import Contact, Content, DateTime, Location, Entity
from typing import Callable, Optional


class MessageEntity(Entity):
    date_time: DateTime
    sender: Contact
    content: Content


class MessageStatus(Entity, Resolvable):
    pass


class MessageContentType(Entity, Resolvable):
    pass

