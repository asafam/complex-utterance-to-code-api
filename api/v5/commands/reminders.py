from typing import Iterable, Union, Optional
from typing.generic import Contact, DateTime, Entity
from typing.reminders import Todo, Reminder
from typing.calendar import CalendarEvent


def create_reminder(
    date_time: Optional[DateTime] = None,
    person_reminded: Optional[Contact] = None,
    todo: Optional[Todo] = None,
    calendar_event: Optional[CalendarEvent] = None,
) -> Reminder:
    raise NotImplementedError


def delete_reminders(
    reminders: Optional[Union[Reminder, Iterable[Reminder]]] = None
) -> bool:
    raise NotImplementedError
