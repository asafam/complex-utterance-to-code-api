from __future__ import annotations
from abc import abstractclassmethod
from generic import Contact, Content, DateTime, Location, Entity
from resolvable import Resolvable
from typing import Callable, Optional


class Reminder(Entity):
    date_time: DateTime
    person_reminded: Contact
    exact_content: Content
