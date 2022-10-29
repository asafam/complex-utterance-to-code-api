from entities.weather import WeatherAttribute, WeatherForecastEntity
from actions.weather import Weather
from providers.data_model import DataModel
from entities.generic import *
from datetime import datetime

def test_simple():
    """
    Utterance: Is it going to drizzle this weekend?
    """
    DataModel.append(DateTime(
        text="this weekend",
        value=datetime(2022, 10, 8)
    ))
    DataModel.append(DateTime(
        text="this weekend",
        value=datetime(2022, 10, 9)
    ))
    DataModel.append(WeatherAttribute(
        text="drizzle",
        value="rain"
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=datetime(2022, 10, 8),
        weather_attribute="rain"
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=datetime(2022, 10, 9),
        weather_attribute="rain"
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=datetime(2022, 10, 10),
        weather_attribute="rain"
    ))

    date_time = DateTime.resolve_from_text("this weekend")
    weather_attribute = WeatherAttribute.resolve_from_text("drizzle")
    weather_forecasts = Weather.find_weather_forecasts(
        date_time=date_time,
        weather_attribute=weather_attribute
    )

    assert len(list(weather_forecasts)) == 2
    

    """
    What will the weather be in two hours, and remind me to go running then.
    """
    DataModel.append(DateTime(
        text="this weekend",
        value=datetime(2022, 10, 8)
    ))
    DataModel.append(DateTime(
        text="this weekend",
        value=datetime(2022, 10, 9)
    ))
    DataModel.append(WeatherAttribute(
        text="drizzle",
        value="rain"
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=datetime(2022, 10, 8),
        weather_attribute="rain"
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=datetime(2022, 10, 9),
        weather_attribute="rain"
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=datetime(2022, 10, 10),
        weather_attribute="rain"
    ))

    date_time = DateTime.resolve_from_text("this weekend")
    weather_attribute = WeatherAttribute.resolve_from_text("drizzle")
    weather_forecasts = Weather.find_weather_forecasts(
        date_time=date_time,
        weather_attribute=weather_attribute
    )


    assert len(list(weather_forecasts)) == 2