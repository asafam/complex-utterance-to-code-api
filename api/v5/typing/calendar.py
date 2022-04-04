from __future__ import annotations
from abc import abstractclassmethod
from typing.generic import Contact, DateTime, Location, Resolveable, Entity
from typing import Callable, Optional


class CalendarEventCategory(Entity, Resolveable):
    pass


class CalendarEventName(Entity, Resolveable):
    pass


class CalendarName(Entity, Resolveable):
    pass


class CalendarEvent(Entity):
    date_time: DateTime
    location: Location
    event_name: CalendarEventName
    event_category: CalendarEventCategory
    calendar: CalendarName

    @abstractclassmethod
    def get_predicate(
        CalendarEvent,
        date_time: Optional[DateTime] = None,
        location: Optional[Contact] = None,
        event_name: Optional[CalendarEventName] = None,
        event_category: Optional[CalendarEventCategory] = None,
    ) -> Callable[[CalendarEvent], bool]:
        raise NotImplementedError
