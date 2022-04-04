from api.v5.typing.weather import WeatherForecast
from typing.generic import Contact, DateTime, Location
from typing.navigation import NavigationRoute
from typing.weather import WeatherCondition
from typing.calendar import CalendarEventName
from queries import calendar, messages, navigation, weather
from commands import reminders as reminders_command
from commands import responder as responder_command
from commands import timer as timer_command
from data_utils import first, last


"""
Example: "Directions from Monteray to San Francisco"
"""
monteray = Location.resolve_from_text("Monteray")
san_francisco = Location.resolve_from_text("San Francisco")

directions = navigation.get_directions(source=monteray, destination=san_francisco)

responder_command.default_responder(response=directions)


"""
Example: "Tell me the weather in Fairlawn, New Jersey"
"""
location = Location.resolve_from_text("Fairlawn, New Jersey")

weather_forecasts = weather.get_weather_forecasts(location=location)

responder_command.default_responder(response=weather_forecasts)


"""
Example: "Check the last message that Kathy sent"
"""
contact = Contact.resolve_from_text("Kathy")

messages = messages.get_messages(sender=contact)
message = last(messages)

responder_command.default_responder(response=message)


"""
Example: ”Tell me the weather even though it is early”
"""
weather_forcasts = weather.get_weather_forecasts()

responder_command.default_responder(response=weather_forcasts)


"""
Example: "If I take 290 what time will I be in Johnson City?"
"""
route = NavigationRoute.resolve_from_text("290")
location = Location.resolve_from_text("Johnson City")
estimated_arrival = navigation.get_estimated_arrival(destination=location, route=route)
responder_command.default_responder(response=estimated_arrival)


"""
Example: "When I need to leave for class to be there at 8 am"
"""
class_event = CalendarEventName.resolve_from_text("class")
events = calendar.get_calendar_events(event_name=class_event)
event = first(events)
location = event.location

date_time = DateTime.resolve_from_text("8 am")

estimated_departure = navigation.get_estimated_departure(
    destination=location, arrival_date_time=date_time
)

responder_command.default_responder(response=estimated_departure)


"""
Example: ”Will it be mostly raining this weekend?”
"""
date_time = DateTime.resolve_from_text("this weekend")
weekend_weather = weather.get_weather_forecasts(date_time=date_time)

raining_weekend_weather = filter(
    WeatherForecast.get_predicate(
        weather_condition=WeatherCondition.resolve_from_text("raining")
    ),
    weekend_weather,
)

mostly_raining = (len(list(raining_weekend_weather)) / len(list(weekend_weather))) > 0.5
responder_command.default_responder(response=mostly_raining)
