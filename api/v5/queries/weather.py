from typing import Iterable, Optional
from typing.generic import DateTime, Location
from typing.weather import WeatherCondition, WeatherForecast


def get_weather_forecasts(
    date_time: Optional[DateTime] = None,
    location: Optional[Location] = None,
    weather_condition: Optional[WeatherCondition] = None,
) -> Iterable[WeatherForecast]:
    raise NotImplementedError
