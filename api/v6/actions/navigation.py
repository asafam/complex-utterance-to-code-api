from abc import abstractclassmethod
from __future__ import annotations
from entities.generic import DateTime, Location, TimeDuration
from entities.navigation import *
from typing import Iterable, Optional


class NavigationEstimation():
    duration: TimeDuration
    source: Location
    destination: Location

    @abstractclassmethod
    def find_directions(
        cls,
        origin: Optional[Location],
        destination: Optional[Location],
        departure_date_time: Optional[DateTime],
        avoid_nav_road_condition: Optional[NavigationRoadCondition],
        nav_travel_method: Optional[NavigationTravelMethod]
    ) -> Iterable[NavigationDirectionEntity]:
        raise NotImplementedError
    
    @abstractclassmethod
    def find_distance(
        cls,
        origin: Optional[Location],
        destination: Optional[Location],
        departure_date_time: Optional[DateTime],
        avoid_nav_road_condition: Optional[NavigationRoadCondition],
        nav_travel_method: Optional[NavigationTravelMethod]
    ) -> Iterable[NavigationDistanceEntity]:
        raise NotImplementedError
    
    @abstractclassmethod
    def find_duration(
        cls,
        origin: Optional[Location],
        destination: Optional[Location],
        departure_date_time: Optional[DateTime],
        avoid_nav_road_condition: Optional[NavigationRoadCondition],
        nav_travel_method: Optional[NavigationTravelMethod]
    ) -> Iterable[NavigationDistanceEntity]:
        raise NotImplementedError

    @abstractclassmethod
    def find_estimated_arrival(
        cls,
        origin: Optional[Location] = None,
        destination: Optional[Location] = None,
        departure_date_time: Optional[DateTime] = None,
        avoid_nav_road_condition: Optional[NavigationRoadCondition] = None,
        nav_travel_method: Optional[NavigationTravelMethod] = None
    ) -> Iterable[NavigationEstimatedArrivalEntity]:
        raise NotImplementedError

    @abstractclassmethod
    def find_estimated_departure(
        cls,
        origin: Optional[Location],
        destination: Optional[Location],
        departure_date_time: Optional[DateTime],
        arrival_date_Time: Optional[DateTime],
        avoid_nav_road_condition: Optional[NavigationRoadCondition],
        nav_travel_method: Optional[NavigationTravelMethod]
    ) -> Iterable[NavigationEstimatedDepartureEntity]:
        raise NotImplementedError

    @abstractclassmethod
    def find_traffic_info(
        cls,
        location: Optional[Location],
        origin: Optional[Location],
        destination: Optional[Location],
        date_time: Optional[DateTime],
        departure_date_time: Optional[DateTime],
        avoid_nav_road_condition: Optional[NavigationRoadCondition],
        nav_travel_method: Optional[NavigationTravelMethod]
    ) -> Iterable[NavigationTrafficInfoEntity]:
        raise NotImplementedError

