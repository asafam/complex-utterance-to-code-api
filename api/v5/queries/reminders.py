from typing import Iterable, Optional
from typing.generic import Contact, DateTime
from typing.reminders import Todo, Reminder
from typing.calendar import CalendarEvent
from exceptions import exception_handler


@exception_handler
def get_reminders(
    person_reminded: Optional[Contact] = None,
    date_time: Optional[DateTime] = None,
    todo: Optional[Todo] = None,
    calendar_event: Optional[CalendarEvent] = None,
) -> Iterable[Reminder]:
    raise NotImplementedError
