from typing.apps import AppName
from typing.calendar import CalendarEventName
from typing.generic import Contact, DateTime, Location
from typing.message import MessageContent
from typing.navigation import TrafficCondition
from typing.reminders import Todo
from typing.weather import WeatherCondition, WeatherForecast, WeatherTemperature
from queries import apps, calendar, messages, navigation, reminders, weather
from commands import messages as messages_command
from commands import reminders as reminders_command
from commands import responder as responder_command
from commands import apps as apps_command
from data_utils import first, last


"""
Example: "Remind me to bring a coat, if it rains"
"""

rains = WeatherCondition.resolve_from_text("rains")
weather_rains = weather.get_weather_forecasts(weather_condition=rains)

if weather_rains:
    me = Contact.resolve_from_text("me")
    todo = Todo.resolve_from_text("to bring a coat")
    reminders_command.create_reminder(person_reminded=me, todo=todo)


"""
Example: "Provided that it rains tomorrow set a reminder to leave 15 minutes earlier"
"""

rains = WeatherCondition.resolve_from_text("rains")
tomorrow = DateTime.resolve_from_text("tomorrow")
weather_rains = weather.get_weather_forecasts(date_time=tomorrow, weather_condition=rains)

if weather_rains:
    todo = Todo.resolve_from_text("to leave 15 minutes earlier")
    reminders_command.create_reminder(todo=todo)


"""
Example: "If it rains then at remind me tonight to bring a coat, if it is less than 40 degrees"
"""

rains = WeatherCondition.resolve_from_text("rains")
weather_rains = weather.get_weather_forecasts(weather_condition=rains)

if weather_rains:
    temperature_40 = filter(WeatherForecast.get_predicate(temperature="less than 40 degrees"), weather_rains)
    
    if len(list(temperature_40)) == 0:
        me = Contact.resolve_from_text("me")
        tonight = DateTime.resolve_from_text("tonight")
        todo = Todo.resolve_from_text("to leave 15 minutes earlier")
        reminders_command.create_reminder(date_time=tonight, person_reminded=me, todo=todo)



"""
Example: "If there is traffic in the city tell Mary that I will be late, otherwise tell her I will be on time"
"""

traffic = TrafficCondition.resolve_from_text("traffic")
city = Location.resolve_from_text("in the city")
traffic_info = navigation.get_traffic_info(location=city, traffic_condition=traffic)

if traffic_info:
    mary = Contact.resolve_from_text("Mary")
    message_content = MessageContent.resolve_from_text("I will be late")
    messages_command.create_message(exact_content=message_content, recipient=mary)
    
else:
    her = Contact.resolve_from_text("her")
    message_content = MessageContent.resolve_from_text("I will be on time")
    messages_command.create_message(exact_content=message_content, recipient=her)


"""
Example: "Provided that I have a reminder or that I got a message from Jane, start me up the yoga app and tell me when I need to leave for class unless it's raining"
"""

i = Contact.resolve_from_text("I")
reminder = reminders.get_reminders(person_reminded=i)

i = Contact.resolve_from_text("I")
jane = Contact.resolve_from_text("Jane")
message = messages.get_messages(recipient=i, sender=jane)

if reminder or message:
    yoga_app = AppName.resolve_from_text("the yoga app")
    apps = apps.get_apps(app_name=yoga_app)
    app = first(apps)
    apps_command.open(app=app)
    
    rains = WeatherCondition.resolve_from_text("raining")
    weather_raining = weather.get_weather_forecasts(weather_condition=rains)

    if  len(list(weather_raining)) == 0:
        class_event_name = CalendarEventName.resolve_from_text("class")
        events = calendar.get_calendar_events(event_name=class_event_name)
        class_event = first(events)
        class_location = class_event.location
        leave_for_class = navigation.get_estimated_departure(destination=class_location)
        responder_command.default_responder(response=leave_for_class)
    
    