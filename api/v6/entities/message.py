from abc import abstractclassmethod
from __future__ import annotations
from entities.entity import Entity
from entities.resolvable import Resolvable
from entities.generic import Contact, Content, DateTime, Location
from typing import Callable, Optional


class MessageEntity(Entity):
    date_time: DateTime
    sender: Contact
    content: Content


class MessageStatus(Entity, Resolvable):
    pass


class MessageContentType(Entity, Resolvable):
    pass

