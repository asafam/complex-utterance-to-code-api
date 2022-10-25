from __future__ import annotations
from abc import abstractclassmethod
from entities.generic import Contact, DateTime, Location, Entity
from resolvable import Resolvable
from typing import Callable, Optional


class AppName(Entity, Resolvable):
    pass


class App(Entity):
    app_name: AppName
