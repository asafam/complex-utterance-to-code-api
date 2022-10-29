from entities.weather import WeatherAttribute, WeatherForecastEntity
from actions.weather import Weather
from providers.data_model import DataModel
from entities.generic import *
from datetime import datetime

    
def test_complex():
    """
    What will the weather be in two hours, and remind me to go running then.
    """
    DataModel.append(DateTime(
        text="in 2 hours",
        value=datetime(2022, 10, 8)
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

    
    date_time = DateTime.resolve_from_text("in two hours")
    weather_forecast = Weathery.find_weather_forecasts(
        date_time=date_time
    )
    Responder.respond(response=weather_forecast)

    content = Content.resolve_from_text("go running")
    person_reminded = Contact.resolve_from_text("me")
    create_reminder(
        content=content, 
        person_reminded=person_reminded, 
        date_time=date_time
    )


    assert len(list(weather_forecasts)) == 2