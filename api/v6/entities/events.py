from __future__ import annotations
from abc import abstractclassmethod
from generic import Contact, Content, DateTime, Location
from entities.entity import Entity
from entities.resolvable import Resolvable
from resolvable import Resolvable

from typing import Callable, Optional


class EventName(Entity, Resolvable):
    pass


class EventCalendar(Entity, Resolvable):
    pass


class EventType(Entity, Resolvable):
    pass


class EventEntity(Entity):
    pass


class EventTicketEntity(Entity):
    pass
