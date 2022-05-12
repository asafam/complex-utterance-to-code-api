from abc import abstractclassmethod
from typing import Iterable, Optional
from typing.generic import Contact, Content, DateTime
from typing.reminders import Reminder
from exceptions.exceptions import exception_handler

class RemindersQuery():
    
    @exception_handler
    @abstractclassmethod
    def get_reminders(
        cls,
        person_reminded: Optional[Contact] = None,
        date_time: Optional[DateTime] = None,
        exact_content: Optional[Content] = None,
    ) -> Iterable[Reminder]:
        raise NotImplementedError
    
    class NavigationQuery:
    @abstractclassmethod
    def get_directions(
        date_time: Optional[DateTime] = None,
        destination: Optional[Location] = None,
        source: Optional[Location] = None,
    ) -> Iterable[NavigationDirection]:
        raise NotImplementedError

    @abstractclassmethod
    def get_estimated_arrival(
        departure_date_time: Optional[DateTime] = None,
        destination: Optional[Location] = None,
        source: Optional[Location] = None,
        route: Optional[NavigationRoute] = None,
    ) -> Iterable[NavigationEstimation]:
        raise NotImplementedError

    @abstractclassmethod
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
