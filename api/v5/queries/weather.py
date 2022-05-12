from abc import abstractclassmethod
from typing import Iterable, Optional
from typing.generic import DateTime, Location
from typing.weather import WeatherCondition, WeatherForecast

class WeatherQuery():
    
    @abstractclassmethod
    def get_weather_forecasts(
        cls,
        date_time: Optional[DateTime] = None,
        location: Optional[Location] = None,
        weather_condition: Optional[WeatherCondition] = None,
    ) -> Iterable[WeatherForecast]:
        raise NotImplementedError
