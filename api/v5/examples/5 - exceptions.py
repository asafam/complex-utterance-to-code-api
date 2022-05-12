from itertools import groupby
from typing.calendar import (
    CalendarEvent,
    CalendarEventCategory,
    CalendarEventName,
    CalendarName,
)
from typing.generic import Contact, DateTime, Location
from typing.message import Content
from typing.navigation import TrafficCondition
from typing.reminders import Content
from typing.weather import WeatherCondition, WeatherTemperature
from queries import calendar, messages, navigation, reminders, weather
from commands.calendar import CalendarCommand
from commands.messages import MessagesCommand
from commands.reminders import RemindersCommand
from commands.responder import ResponderCommand
from data_utils import first, last, day_of_the_week
from exceptions.exceptions import NoSuchValueException

"""
Execution exception example: Cancel all my meetings on February 30
"""
try:
    d = DateTime.resolve_from_text("February 30")  # <- should raise recovery exception
    meetings = CalendarQuery.get_calendar_events(date_time=d)
    CalendarCommand.delete_calendar_events(events=meetings)
except NoSuchValueException as e:
    pass

"""
Execution exception example: Provided that it rains tomorrow set a reminder
"""

rains = WeatherCondition.resolve_from_text("rains")
tomorrow = DateTime.resolve_from_text("tomorrow")
weather_rains = WeatherQuery.get_weather_forecasts(
    date_time=tomorrow, weather_condition=rains
)

if weather_rains:
    RemindersCommand.create_reminder()  # <- should raise recovery exception

"""
Example: "If there is traffic tell Mary that I will be late"
"""

traffic = TrafficCondition.resolve_from_text("traffic")
traffic_info = NavigationQuery.get_traffic_info(
    traffic_condition=traffic
)  # <- should raise recovery exception

if traffic_info:
    mary = Contact.resolve_from_text("Mary")
    message_content = Content.resolve_from_text("I will be late")
    MessagesCommand.send_message(exact_content=message_content, recipient=mary)
