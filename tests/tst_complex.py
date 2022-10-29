from entities.weather import WeatherAttribute, WeatherForecastEntity
from actions.weather import Weather
from actions.reminders import Reminders
from actions.responder import Responder
from providers.data_model import DataModel
from entities.generic import *
from entities.reminder import *
from datetime import datetime

    
def test_complex():
    """
    What will the weather be in two hours, and remind me then to go running.
    """
    data_date_time = DateTime(
        text="in 2 hours",
        value=datetime(2022, 10, 8, 16, 15)
    )
    DataModel.append(data_date_time)
    data_person_reminded = Contact(
        text="me",
        value="Louis Armstrong"
    )
    data_content = Content(
        text="go running",
        value="go running"
    )
    DataModel.append(ReminderEntity(
        person_reminded=data_person_reminded,
        date_time=data_date_time,
        content=data_content
    ))

    
    date_time = DateTime.resolve_from_text("in two hours")
    weather_forecasts = Weather.find_weather_forecasts(
        date_time=date_time
    )
    Responder.respond(response=weather_forecasts)

    content = Content.resolve_from_text("go running")
    person_reminded = Contact.resolve_from_text("me")
    reminder = Reminders.create_reminder(
        content=content, 
        person_reminded=person_reminded, 
        date_time=date_time
    )

    
    assert len(list(weather_forecasts)) == 1
    assert list(weather_forecasts)[0].data.get('date_time') == datetime(2022, 10, 8, 16, 15)