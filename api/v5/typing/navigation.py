from abc import abstractclassmethod
from __future__ import annotations
from resolveable import Resolveable
from typing.generic import Entity, DateTime, Location
from typing import Callable, Optional


class NavigationDirection(Entity):
    pass


class NavigationEstimation(Entity):
    duration: DateTime
    source: Location
    destination: Location

    @abstractclassmethod
    def get_predicate(
        NavigationEstimation,
        duration: Optional[DateTime] = None,
        source: Optional[Location] = None,
        destination: Optional[Location] = None,
    ) -> Callable[[NavigationEstimation], bool]:
        raise NotImplementedError


class NavigationRoute(Entity, Resolveable):
    pass


class TrafficCondition(Entity, Resolveable):
    pass
