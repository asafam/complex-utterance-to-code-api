from api.v5.commands.messages import MessagesCommand
from api.v5.commands.reminders import RemindersCommand
from typing.apps import AppName
from typing.calendar import CalendarEventName
from typing.generic import Contact, DateTime, Location
from typing.message import Content
from typing.navigation import TrafficCondition
from typing.reminders import Content
from typing.weather import WeatherCondition, WeatherForecast, WeatherTemperature
from queries.apps import AppsQuery
from queries.navigation import NavigationQuery
from queries.weather import WeatherQuery
from queries.messages import MessagesQuery
from queries.calendar import CalendarQuery
from queries.reminders import RemindersQuery
from commands.reminders import RemindersCommand
from commands.responder import ResponderCommand
from commands.apps import AppsCommand
from data_utils import first, last


"""
Example: "Remind me to bring a coat, if it rains"
"""

weather_condition = WeatherCondition.resolve_from_text("rains")
weather_forecasts = WeatherQuery.get_weather_forecasts(weather_condition=weather_condition)
condition = len(list(weather_forecasts)) > 0
if condition:
    contact = Contact.resolve_from_text("me")
    content = Content.resolve_from_text("to bring a coat")
    RemindersCommand.create_reminder(person_reminded=contact, exact_content=content)


"""
Example: "Provided that it rains tomorrow set a reminder to leave 15 minutes earlier"
"""

weather_condition = WeatherCondition.resolve_from_text("rains")
date_time = DateTime.resolve_from_text("tomorrow")
weather_forecasts = WeatherQuery.get_weather_forecasts(date_time=date_time, weather_condition=weather_condition)
condition = len(list(weather_forecasts)) > 0
if condition:
    exact_content = Content.resolve_from_text("to leave 15 minutes earlier")
    RemindersCommand.create_reminder(exact_content=exact_content)


"""
Example: "If it rains then remind me tonight to bring a coat, if it is less than 40 degrees"
"""

weather_condition = WeatherCondition.resolve_from_text("rains")
weather_rains = WeatherQuery.get_weather_forecasts(weather_condition=weather_condition)
condition = len(list(weather_forecasts)) > 0
if condition:
    temperature = WeatherTemperature.resolve_from_text("less than 40 degrees")
    weather_forecasts = filter(WeatherForecast.get_predicate(temperature=temperature), weather_forecasts)
    condition = len(list(weather_forecasts)) > 0
    if condition:
        contact = Contact.resolve_from_text("me")
        date_time = DateTime.resolve_from_text("tonight")
        content = Content.resolve_from_text("to leave 15 minutes earlier")
        RemindersCommand.create_reminder(date_time=date_time, person_reminded=contact, exact_content=content)



"""
Example: "If there is traffic in the city tell Mary that I will be late, otherwise tell her I will be on time"
"""

traffic_condition = TrafficCondition.resolve_from_text("traffic")
location = Location.resolve_from_text("in the city")
traffic_info = NavigationQuery.get_traffic_info(location=location, traffic_condition=traffic_condition)

if traffic_info:
    contact = Contact.resolve_from_text("Mary")
    content = Content.resolve_from_text("I will be late")
    MessagesCommand.send_message(exact_content=content, recipient=contact)
    
else:
    contact = Contact.resolve_from_text("her")
    content = Content.resolve_from_text("I will be on time")
    MessagesCommand.send_message(exact_content=content, recipient=contact)


"""
Example: "Provided that I have a reminder or that I got a message from Jane, start me up the yoga app and tell me when I need to leave for class unless it's raining"
"""

contact = Contact.resolve_from_text("I")
reminder = RemindersQuery.get_reminders(person_reminded=contact)

contact = Contact.resolve_from_text("I")
contact2 = Contact.resolve_from_text("Jane")
message = MessagesQuery.get_messages(recipient=contact, sender=contact2)

if reminder or message:
    app_name = AppName.resolve_from_text("the yoga app")
    apps = AppsQuery.get_apps(app_name=app_name)
    app = first(apps)
    AppsCommand.open(app=app)
    
    weather_condition = WeatherCondition.resolve_from_text("raining")
    weather_raining = WeatherQuery.get_weather_forecasts(weather_condition=weather_condition)
    condition = len(list(weather_raining)) > 0
    if  not condition:
        event_name = CalendarEventName.resolve_from_text("class")
        events = CalendarQuery.get_calendar_events(event_name=event_name)
        class_event = first(events)
        location = class_event.location
        estimated_departure = NavigationQuery.get_estimated_departure(destination=location)
        ResponderCommand.default_responder(response=estimated_departure)
    
    