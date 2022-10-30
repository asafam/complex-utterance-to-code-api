from entities.weather import WeatherAttribute, WeatherForecastEntity
from actions.weather import Weather
from actions.responder import Responder
from providers.data_model import DataModel
from entities.generic import *
from datetime import datetime

def test_simple():
    """
    Utterance: Is it going to drizzle this weekend?
    """
    # test data
    DataModel.initialize()
    data_date_time1 = DateTime(
        text="this weekend",
        value=datetime(2022, 10, 8, 0, 0)
    )
    data_date_time2 = DateTime(
        text="this weekend",
        value=datetime(2022, 10, 9, 0, 0)
    )
    data_date_time3 = DateTime(
        text="this weekend",
        value=datetime(2022, 10, 10, 0, 0)
    )
    DataModel.append(data_date_time1)
    DataModel.append(data_date_time2)
    data_weather_attribute = WeatherAttribute(
        text="drizzle",
        value="rain"
    )
    data_weather_attribute_x = WeatherAttribute(
        text="cloudy",
        value="cloudy"
    )
    DataModel.append(data_weather_attribute)
    DataModel.append(WeatherForecastEntity(
        date_time=data_date_time1,
        weather_attribute=data_weather_attribute
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=data_date_time2,
        weather_attribute=data_weather_attribute
    ))
    DataModel.append(WeatherForecastEntity(
        date_time=data_date_time3,
        weather_attribute=data_weather_attribute_x
    ))

    # code block to test
    date_time = DateTime.resolve_many_from_text("this weekend")
    weather_attribute = WeatherAttribute.resolve_from_text("drizzle")
    weather_forecasts = Weather.find_weather_forecasts(
        date_time=date_time,
        weather_attribute=weather_attribute
    )
    Responder.respond(response=weather_forecasts)

    #  assertion tests
    assert len(list(weather_forecasts)) == 2
    assert list(weather_forecasts)[0].data.get('date_time') == data_date_time1
    assert list(weather_forecasts)[0].data.get('weather_attribute') == data_weather_attribute
    assert list(weather_forecasts)[1].data.get('date_time') == data_date_time2
    assert list(weather_forecasts)[1].data.get('weather_attribute') == data_weather_attribute
    