from __future__ import annotations
from abc import abstractclassmethod
from typing.generic import Contact, DateTime, Location, Resolveable, Entity
from typing import Callable, Optional


class Todo(Entity, Resolveable):
    pass


class Reminder(Entity):
    date_time: DateTime
    person_reminded: Contact
    todo: Todo

    @abstractclassmethod
    def get_predicate(
        Reminder,
        date_time: Optional[DateTime] = None,
        person_reminded: Optional[Contact] = None,
        todo: Optional[Todo] = None,
    ) -> Callable[[Reminder], bool]:
        raise NotImplementedError
