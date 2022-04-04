from ctypes import util
from typing.generic import Contact, DateTime, Location
from typing.navigation import NavigationRoute
from typing.weather import WeatherCondition
from typing.calendar import CalendarEventName
from typing.timer import Timer
from queries import calendar, messages, navigation, reminders, weather
from commands import reminders as reminders_command
from commands import responder as responder_command
from commands import timer as timer_command
from data_utils import first, last


# Example: "Pause the timer, stop it, and restart it"

timer1 = Timer.resolve_from_text("the timer")
timer_command.pause(timer=timer1)

timer2 = Timer.resolve_from_text("it")
timer_command.stop(timer=timer2)

timer3 = Timer.resolve_from_text("it")
timer_command.restart(timer=timer3)


# Example: "Tell me the weather forecast and delete the last reminder"

weather_forecast = weather.get_weather_forecasts()

responder_command.default_responder(response=weather_forecast)

all_reminders = reminders.get_reminders()
reminder = last(all_reminders)

reminders_command.delete_reminders(reminders=reminder)

