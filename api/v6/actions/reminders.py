from abc import abstractclassmethod, abstractmethod
from typing import Any, Iterable, Mapping, Union, Optional
from entities.resolvable import Resolvable
from entities.generic import *
from entities.reminder import Content, Reminder
from entities.calendar import CalendarEvent
from exceptions.exceptions import UnderspecificationException


class Reminders(Resolvable):
    @classmethod
    def create_reminder(
        cls,
        person_reminded: Contact,
        content: Content,
        date_time: Optional[DateTime] = None,
        calendar_event: Optional[CalendarEvent] = None,
        recovered_args: Optional[Mapping[str, Any]] = None,
    ) -> Reminder:
        if not content:
            payload = {
                "date_time": date_time,
                "person_reminded": person_reminded,
                "content": content,
                "calendar_event": calendar_event,
                "recovered_args": recovered_args,
            }
            raise UnderspecificationException(
                payload=payload,
                recovery_prompt="What should be reminded?",
                message="content argument is missing",
            )
        raise NotImplementedError

    # @exception_handler
    @abstractclassmethod
    def find_reminders(
        cls,
        person_reminded: Optional[Contact] = None,
        date_time: Optional[DateTime] = None,
        content: Optional[Content] = None,
    ) -> Iterable[Reminder]:
        raise NotImplementedError

    @abstractclassmethod
    def delete_reminders(cls, reminders: Union[Reminder, Iterable[Reminder]]) -> bool:
        data = []

        raise NotImplementedError
