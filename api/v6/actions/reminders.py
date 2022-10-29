from abc import abstractclassmethod, abstractmethod
from typing import Any, Iterable, Mapping, Union, Optional
from api.v6.entities.resolvable import Resolvable
from entities.generic import Contact, DateTime, Entity
from entities.reminder import Content, Reminder
from entities.calendar import CalendarEvent
from exceptions.exceptions import UnderspecificationException


class Reminders(Resolvable):
    @classmethod
    def create_reminder(
        cls,
        date_time: Optional[DateTime] = None,
        person_reminded: Optional[Contact] = None,
        exact_content: Optional[Content] = None,
        calendar_event: Optional[CalendarEvent] = None,
        recovered_args: Optional[Mapping[str, Any]] = None,
    ) -> Reminder:
        if not exact_content:
            payload = {
                "date_time": date_time,
                "person_reminded": person_reminded,
                "exact_content": exact_content,
                "calendar_event": calendar_event,
                "recovered_args": recovered_args,
            }
            raise UnderspecificationException(
                payload=payload,
                recovery_prompt="What should be reminded?",
                message="exact_content argument is missing",
            )
        raise NotImplementedError
    
    @exception_handler
    @abstractclassmethod
    def find_reminders(
        cls,
        person_reminded: Optional[Contact] = None,
        date_time: Optional[DateTime] = None,
        exact_content: Optional[Content] = None,
    ) -> Iterable[Reminder]:
        raise NotImplementedError

    @abstractclassmethod
    def delete_reminders(
        cls, 
        reminders: Union[Reminder, Iterable[Reminder]]
    ) -> bool:
        data = []
        
        raise NotImplementedError
