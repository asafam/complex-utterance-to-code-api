from __future__ import annotations
from abc import abstractclassmethod
from generic import Contact, Content, DateTime, Location
from entities.entity import Entity
from entities.resolvable import Resolvable
from resolvable import Resolvable

from typing import Callable, Optional


class EventName(Entity, Resolvable):
    pass


class EventCategory(Entity, Resolvable):
    pass


class Event(Entity):
    date_time: DateTime
    location: Location
    event_name: EventName
    event_category: EventCategory

    @abstractclassmethod
    def get_predicate(
        Event,
        date_time: Optional[DateTime] = None,
        location: Optional[Location] = None,
        event_name: Optional[EventName] = None,
        event_category: Optional[EventCategory] = None,
    ) -> Callable[[Event], bool]:
        raise NotImplementedError
