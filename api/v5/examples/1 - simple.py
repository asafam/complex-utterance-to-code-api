from typing.generic import Contact, DateTime, Location
from typing.navigation import NavigationRoute
from typing.weather import WeatherCondition, WeatherForecast
from typing.calendar import CalendarEventName
from queries.navigation import NavigationQuery
from queries.weather import WeatherQuery
from queries.messages import MessagesQuery
from queries.calendar import CalendarQuery
from commands.reminders import RemindersCommand
from commands.responder import ResponderCommand
from commands.timer import TimerCommand
from data_utils import first, last


"""
Example: "Directions from Monteray to San Francisco"
"""
source = Location.resolve_from_text("Monteray")
destination = Location.resolve_from_text("San Francisco")

directions = NavigationQuery.get_directions(source=source, destination=destination)

ResponderCommand.default_responder(response=directions)


"""
Example: "Tell me the weather in Fairlawn, New Jersey"
"""
location = Location.resolve_from_text("Fairlawn, New Jersey")

weather_forecasts = WeatherQuery.get_weather_forecasts(location=location)

ResponderCommand.default_responder(response=weather_forecasts)


"""
Example: "Check the last message that Kathy sent"
"""
contact = Contact.resolve_from_text("Kathy")

messages = MessagesQuery.get_messages(sender=contact)
message = last(messages)

ResponderCommand.default_responder(response=message)


"""
Example: ”Tell me the weather even though it is early”
"""
weather_forcasts = WeatherQuery.get_weather_forecasts()

ResponderCommand.default_responder(response=weather_forcasts)


"""
Example: "If I take 290 what time will I be in Johnson City?"
"""
route = NavigationRoute.resolve_from_text("290")
location = Location.resolve_from_text("Johnson City")
estimated_arrival = NavigationQuery.get_estimated_arrival(
    destination=location, route=route
)
ResponderCommand.default_responder(response=estimated_arrival)


"""
Example: "When I need to leave for class to be there at 8 am"
"""
event_name = CalendarEventName.resolve_from_text("class")
results = CalendarQuery.get_calendar_events(event_name=event_name)
first_result = first(results)
location = first_result.location

date_time = DateTime.resolve_from_text("8 am")

estimated_departure = NavigationQuery.get_estimated_departure(
    destination=location, arrival_date_time=date_time
)

ResponderCommand.default_responder(response=estimated_departure)


"""
Example: ”Will it be mostly raining this weekend?”
"""
date_time = DateTime.resolve_from_text("this weekend")
weather_forecasts = WeatherQuery.get_weather_forecasts(date_time=date_time)

weather_condition = WeatherCondition.resolve_from_text("raining")
weather_forecasts2 = filter(
    WeatherForecast.get_predicate(weather_condition=weather_condition),
    weather_forecasts,
)

result = (len(list(weather_forecasts2)) / len(list(weather_forecasts))) > 0.5
ResponderCommand.default_responder(response=result)
