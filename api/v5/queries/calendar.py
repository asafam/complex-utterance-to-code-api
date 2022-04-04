from typing import Iterable, Optional
from typing.generic import DateTime, Location
from typing.calendar import (
    CalendarEventCategory,
    CalendarEventName,
    CalendarEvent,
    CalendarName,
)


def get_calendar_events(
    date_time: Optional[DateTime] = None,
    location: Optional[Location] = None,
    event_name: Optional[CalendarEventName] = None,
    category: Optional[CalendarEventCategory] = None,
    calendar: Optional[CalendarName] = None,
) -> Iterable[CalendarEvent]:
    raise NotImplementedError
