from abc import abstractclassmethod
from typing import Iterable, Union, Optional
from api.v6.entities.resolvable import Resolvable
from entities.generic import *
from entities.calendar import *


class Calendar(Resolvable):
    
    @abstractclassmethod
    def create_calendar_event(
        cls,
        date_time: Optional[DateTime] = None,
        location: Optional[Location] = None,
        event_name: Optional[CalendarEventName] = None,
        category: Optional[CalendarEventCategory] = None,
        calendar: Optional[CalendarName] = None,
    ) -> CalendarEvent:
        raise NotImplementedError

    @abstractclassmethod
    def delete_calendar_events(
        cls, events: Optional[Union[CalendarEvent, Iterable[CalendarEvent]]] = None
    ) -> bool:
        raise NotImplementedError
    
    @abstractclassmethod
    def find_calendar_events(
        cls,
        date_time: Optional[DateTime] = None,
        location: Optional[Location] = None,
        event_name: Optional[CalendarEventName] = None,
        event_category: Optional[CalendarEventCategory] = None,
        calendar: Optional[CalendarName] = None,
    ) -> Iterable[CalendarEvent]:
        raise NotImplementedError
