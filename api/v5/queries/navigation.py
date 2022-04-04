from typing import Optional, Iterable
from typing.generic import DateTime, Location
from typing.navigation import (
    NavigationDirection,
    NavigationEstimation,
    NavigationRoute,
    TrafficCondition,
)


def get_directions(
    date_time: Optional[DateTime] = None,
    destination: Optional[Location] = None,
    source: Optional[Location] = None,
) -> Iterable[NavigationDirection]:
    raise NotImplementedError


def get_estimated_arrival(
    departure_date_time: Optional[DateTime] = None,
    destination: Optional[Location] = None,
    source: Optional[Location] = None,
    route: Optional[NavigationRoute] = None,
) -> Iterable[NavigationEstimation]:
    raise NotImplementedError


def get_estimated_departure(
    arrival_date_time: Optional[DateTime] = None,
    destination: Optional[Location] = None,
    source: Optional[Location] = None,
    route: Optional[NavigationRoute] = None,
) -> Iterable[NavigationEstimation]:
    raise NotImplementedError


def get_traffic_info(
    date_time: Optional[DateTime] = None,
    location: Optional[Location] = None,
    traffic_condition: Optional[TrafficCondition] = None,
    route: Optional[NavigationRoute] = None,
) -> Iterable[NavigationEstimation]:
    raise NotImplementedError
