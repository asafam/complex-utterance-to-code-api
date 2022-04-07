from typing import Iterable, Union, Optional
from typing.generic import Contact, DateTime, Location
from typing.calendar import CalendarEvent, CalendarEventCategory, CalendarEventName, CalendarName


def create_calendar_event(
    date_time: Optional[DateTime] = None,
    location: Optional[Location] = None,
    event_name: Optional[CalendarEventName] = None,
    category: Optional[CalendarEventCategory] = None,
    calendar: Optional[CalendarName] = None,
) -> CalendarEvent:
    raise NotImplementedError


def delete_calendar_events(
    events: Optional[Union[CalendarEvent, Iterable[CalendarEvent]]] = None
) -> bool:
    raise NotImplementedError
