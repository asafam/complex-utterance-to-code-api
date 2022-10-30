from entities.generic import *
from entities.message import *
from entities.navigation import *
from entities.reminder import *
from entities.weather import *
from actions.messages import Messages
from actions.navigation import Navigation
from actions.reminders import Reminders
from actions.responder import Responder
from actions.weather import Weather
from providers.data_model import DataModel
from datetime import datetime


def test_get_started_complex1():
    """
    What will the weather be in two hours, and remind me then to go running.
    """
    # test data
    DataModel.initialize()
    data_date_time = DateTime(text="in two hours", value=datetime(2022, 10, 8, 16, 15))
    DataModel.append(data_date_time)
    DataModel.append(WeatherForecastEntity(date_time=data_date_time))
    data_person_reminded = Contact(text="me", value="Louis Armstrong")
    DataModel.append(data_person_reminded)
    data_content = Content(text="go running", value="go running")
    DataModel.append(data_content)
    DataModel.append(
        ReminderEntity(
            person_reminded=data_person_reminded,
            date_time=data_date_time,
            content=data_content,
        )
    )

    # code block to test
    date_time = DateTime.resolve_from_text("in two hours")
    weather_forecasts = Weather.find_weather_forecasts(date_time=date_time)
    Responder.respond(response=weather_forecasts)

    content = Content.resolve_from_text("go running")
    person_reminded = Contact.resolve_from_text("me")
    reminder = Reminders.create_reminder(
        content=content, person_reminded=person_reminded, date_time=date_time
    )

    # assertions
    assert len(list(weather_forecasts)) == 1
    assert list(weather_forecasts)[0].data.get("date_time") == data_date_time

    assert reminder.data.get("content") == data_content
    assert reminder.data.get("person_reminded") == data_person_reminded
    assert reminder.data.get("date_time") == data_date_time


def test_get_started_complex2():
    """
    Get directions from Disneyland to my house and text them to Robert.
    """
    # test data
    DataModel.initialize()
    data_origin = Location(text="Disneyland", value="Disneyland")
    DataModel.append(data_origin)
    data_destination = Location(text="my house", value="my house")
    DataModel.append(data_destination)
    data_navigation_direction = NavigationDirectionEntity(
        origin=data_origin,
        destination=data_destination,
    )
    DataModel.append(data_navigation_direction)
    DataModel.append(
        NavigationDirectionEntity(
            origin=data_destination,
            destination=data_origin,
        )
    )
    data_recipient = Contact(text="Robert", value="Robert Lowry")
    DataModel.append(data_recipient)
    data_content = Content(value=[data_navigation_direction])
    DataModel.append(data_content)

    # code block to be tested
    origin = Location.resolve_from_text("Disneyland")
    destination = Location.resolve_from_text("my house")
    navigation_directions = Navigation.find_directions(
        origin=origin, destination=destination
    )

    recipient = Contact.resolve_from_text("Robert")
    content = Content.resolve_from_entity(navigation_directions)
    message = Messages.send_message(recipient=recipient, content=content)

    # assertions
    assert len(list(navigation_directions)) == 1
    assert list(navigation_directions)[0].data.get("origin") == data_origin
    assert list(navigation_directions)[0].data.get("destination") == data_destination

    data_messages = DataModel.get_data(MessageEntity)
    assert len(list(data_messages)) == 1
    assert data_messages[-1].data.get("recipient") == data_recipient
    assert data_messages[-1].data.get("content") == data_content
    
    
def test_get_started_complex3a():
    """
    Remind me to bring an umbrella if it rains tomorrow.
    """
    # test data
    DataModel.initialize()
    data_weather_attribute = WeatherAttribute(text="rains", value="rain")
    DataModel.append(data_weather_attribute)
    data_date_time = DateTime(text="tomorrow", value=datetime(2022, 10, 12, 0, 0))
    DataModel.append(data_date_time)
    DataModel.append(WeatherForecastEntity(weather_attribute=data_weather_attribute, date_time=data_date_time))
    data_person_reminded = Contact(text="me", value="Julian Sochan")
    DataModel.append(data_person_reminded)
    data_content = Content(text="bring an umbrella", value="bring an umbrella")
    DataModel.append(data_content)

    # code block to be tested
    date_time = DateTime.resolve_from_text("tomorrow")
    weather_attribute = WeatherAttribute.resolve_from_text("rains")
    weather_forecasts = Weather.find_weather_forecasts(
        date_time=date_time, 
        weather_attribute=weather_attribute
    )
    expr = len(list(weather_forecasts)) > 0
    if expr:
        person_reminded = Contact.resolve_from_text("me")
        content = Content.resolve_from_text("bring an umbrella")
        reminder = Reminders.create_reminder(
            person_reminded=person_reminded, 
            content=content
        )

    # assertions
    assert len(list(weather_forecasts)) == 1
    assert list(weather_forecasts)[0].data.get("date_time") == data_date_time
    assert list(weather_forecasts)[0].data.get("weather_attribute") == data_weather_attribute

    data_reminders = DataModel.get_data(ReminderEntity)
    assert len(list(data_reminders)) == 1
    assert data_reminders[-1].data.get("person_reminded") == data_person_reminded
    assert data_reminders[-1].data.get("content") == data_content

    
def test_get_started_complex3b():
    """
    Remind me to bring an umbrella if it rains tomorrow.
    """
    # test data
    DataModel.initialize()
    data_weather_attribute1 = WeatherAttribute(text="rains", value="rain")
    DataModel.append(data_weather_attribute1)
    data_weather_attribute2 = WeatherAttribute(text="sunny", value="sun")
    DataModel.append(data_weather_attribute2)
    data_date_time = DateTime(text="tomorrow", value=datetime(2022, 10, 12, 0, 0))
    DataModel.append(data_date_time)
    DataModel.append(WeatherForecastEntity(weather_attribute=data_weather_attribute2, date_time=data_date_time))
    data_person_reminded = Contact(text="me", value="Julian Sochan")
    DataModel.append(data_person_reminded)
    data_content = Content(text="bring an umbrella", value="bring an umbrella")
    DataModel.append(data_content)

    # code block to be tested
    date_time = DateTime.resolve_from_text("tomorrow")
    weather_attribute = WeatherAttribute.resolve_from_text("rains")
    weather_forecasts = Weather.find_weather_forecasts(
        date_time=date_time, 
        weather_attribute=weather_attribute
    )
    expr = len(list(weather_forecasts)) > 0
    if expr:
        person_reminded = Contact.resolve_from_text("me")
        content = Content.resolve_from_text("bring an umbrella")
        reminder = Reminders.create_reminder(
            person_reminded=person_reminded, 
            content=content
        )

    # assertions
    assert len(list(weather_forecasts)) == 0

    data_reminders = DataModel.get_data(ReminderEntity)
    assert len(list(data_reminders)) == 0


def test_get_started_complex4a():
    """
    Show me the traffic to each Whole Food branch in a 10 miles radius.
    """
    # test data
    DataModel.initialize()
    data_location1 = Location(text="each Whole Food branch in a 10 miles radius", value="Whole Food #1")
    DataModel.append(data_location1)
    data_location2 = Location(text="each Whole Food branch in a 10 miles radius", value="Whole Food #2")
    DataModel.append(data_location2)
    data_location3 = Location(text="each Whole Food branch in a 10 miles radius", value="Whole Food #3")
    DataModel.append(data_location3)
    data_location4 = Location(text="Whole Food branch in over a 10 miles radius", value="Whole Food #4")
    DataModel.append(data_location4)
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location1))
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location2))
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location3))
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location4))

    # code block to be tested
    destinations = Location.resolve_many_from_text("each Whole Food branch in a 10 miles radius")
    response = []
    for destination in destinations:
        traffic_info = Navigation.find_traffic_info(destination=destination)
        if traffic_info:
            response.append(traffic_info)
    Responder.respond(response=response)

    # assertions
    assert len(list(destinations)) == 3
    assert len(list(response)) == 3


def test_get_started_complex4b():
    """
    Show me the traffic to each Whole Food branch in a 10 miles radius.
    """
    # test data
    DataModel.initialize()
    data_location1 = Location(text="each Whole Food branch in a 10 miles radius", value="Whole Food #1")
    DataModel.append(data_location1)
    data_location2 = Location(text="each Whole Food branch in a 10 miles radius", value="Whole Food #2")
    DataModel.append(data_location2)
    data_location3 = Location(text="each Whole Food branch in a 10 miles radius", value="Whole Food #3")
    DataModel.append(data_location3)
    data_location4 = Location(text="Whole Food branch in over a 10 miles radius", value="Whole Food #4")
    DataModel.append(data_location4)
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location1))
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location2))
    DataModel.append(NavigationTrafficInfoEntity(destination=data_location4))

    # code block to be tested
    destinations = Location.resolve_many_from_text("each Whole Food branch in a 10 miles radius")
    response = []
    for destination in destinations:
        traffic_info = Navigation.find_traffic_info(destination=destination)
        if traffic_info:
            response.append(traffic_info)
    Responder.respond(response=response)

    # assertions
    assert len(list(destinations)) == 3
    assert len(list(response)) == 2


