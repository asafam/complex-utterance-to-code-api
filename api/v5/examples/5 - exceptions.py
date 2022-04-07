from itertools import groupby
from typing.calendar import (
    CalendarEvent,
    CalendarEventCategory,
    CalendarEventName,
    CalendarName,
)
from typing.generic import Contact, DateTime, Location
from typing.message import MessageContent
from typing.navigation import TrafficCondition
from typing.reminders import Todo
from typing.weather import WeatherCondition, WeatherTemperature
from queries import calendar, messages, navigation, reminders, weather
from commands import calendar as calendar_commands
from commands import messages as messages_command
from commands import reminders as reminders_command
from commands import responder as responder_command
from data_utils import first, last, day_of_the_week
from exceptions import NoSuchValueException

"""
Execution exception example: Cancel all my meetings on February 30
"""
try:
    d = DateTime.resolve_from_text("February 30")  # <- should raise recovery exception
    meetings = calendar.get_calendar_events(date_time=d)
    calendar_commands.delete_calendar_events(events=meetings)
except NoSuchValueException as e:
    pass

"""
Execution exception example: Provided that it rains tomorrow set a reminder
"""

rains = WeatherCondition.resolve_from_text("rains")
tomorrow = DateTime.resolve_from_text("tomorrow")
weather_rains = weather.get_weather_forecasts(
    date_time=tomorrow, weather_condition=rains
)

if weather_rains:
    reminders_command.create_reminder()  # <- should raise recovery exception

"""
Example: "If there is traffic tell Mary that I will be late"
"""

traffic = TrafficCondition.resolve_from_text("traffic")
traffic_info = navigation.get_traffic_info(traffic_condition=traffic) # <- should raise recovery exception

if traffic_info:
    mary = Contact.resolve_from_text("Mary")
    message_content = MessageContent.resolve_from_text("I will be late")
    messages_command.create_message(exact_content=message_content, recipient=mary)
