from abc import abstractclassmethod
from typing import Iterable, Optional
from entities.generic import DateTime, Location
from entities.weather import WeatherAttribute, WeatherForecastEntity

class Weather():
    
    @abstractclassmethod
    def get_weather_forecasts(
        cls,
        date_time: Optional[DateTime] = None,
        location: Optional[Location] = None,
        weather_attribute: Optional[WeatherAttribute] = None,
    ) -> Iterable[WeatherForecastEntity]:
        raise NotImplementedError
