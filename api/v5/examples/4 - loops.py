from itertools import groupby
from typing.calendar import CalendarEvent, CalendarEventCategory, CalendarEventName, CalendarName
from typing.generic import Contact, DateTime, Location
from typing.message import MessageContent
from typing.navigation import TrafficCondition
from typing.reminders import Todo
from typing.weather import WeatherCondition, WeatherTemperature
from queries import calendar, messages, navigation, reminders, weather
from commands import messages as messages_command
from commands import reminders as reminders_command
from commands import responder as responder_command
from data_utils import first, last, day_of_the_week


"""
Example: ”Get the weather in London today and tomorrow”
"""
location = Location.resolve_from_text("London")

today = DateTime.resolve_from_text("today")
tomorrow = DateTime.resolve_from_text("tomorrow")

for date_time in [today, tomorrow]:
    forecasts = weather.get_weather_forecasts(location=location, date_time=date_time)

    responder_command.default_responder(response=forecasts)


"""
Example: "Tell me every stand up show tonight in the city at 8 pm"
"""

standup = CalendarEventCategory.resolve_from_text("stand up show")
tonight = DateTime.resolve_from_text("tonight")
city = Location.resolve_from_text("in the city")

eight_pm = DateTime.resolve_from_text("at 8 pm")

events = calendar.get_calendar_events(
    location=city, date_time=tonight, category=standup
)
events2 = filter(CalendarEvent.get_predicate(date_time=eight_pm), events)

responder_command.default_responder(response=events2)


"""
Example: "Create a reminder for the Monday appointment while cancelling all other reminders for today"
"""
monday  = DateTime.resolve_from_text("Monday")
events = calendar.get_calendar_events(date_time=monday)
appointment = first(events)
reminder = reminders_command.create_reminder(calendar_event=appointment)

today  = DateTime.resolve_from_text("today")
reminders = reminders.get_reminders(date_time=today)
for r in reminders:
    if r != reminder:
        reminders_command.delete_reminders(r)


"""
Example: "Text mom and dad about the Saturday brunch and the matinee"
"""
mom = Contact.resolve_from_text("mom")

dad = Contact.resolve_from_text("dad")

brunch = CalendarEventName.resolve_from_text("Saturday brunch")
saturday = DateTime.resolve_from_text("Saturday")
events = calendar.get_calendar_events(date_time=saturday, event_name=brunch)
saturday_brunch = first(events)

matinee = CalendarEventName.resolve_from_text("the matinee")
events = calendar.get_calendar_events(event_name=matinee)
matinee_event = first(events)

for contact in [mom, dad]:
    for calendar_event in [matinee, saturday_brunch]:
        messages_command.create_message(recipient=contact, exact_content=calendar_event)



"""
Read me the first and last meeting for each day of the week I have on my calendar
"""
week = DateTime.resolve_from_text("the week")
cal = CalendarName.resolve_from_text("my calendar")
meetings = calendar.get_calendar_events(date_time=week, calendar=cal)

meeting_days = list(set(map(lambda x: day_of_the_week(x.date_time), meetings)))
for day in meeting_days:
    daily_meetings = filter(lambda x: day_of_the_week(x.date_time), meetings)
    first_meeting = first(daily_meetings)
    last_meeting = last(daily_meetings) if len(list(daily_meetings)) > 1 else None
    responder_command.default_responder(response=first_meeting)
    if last_meeting:
        responder_command.default_responder(response=last_meeting)

# weekly_meetings = groupby(meetings, lambda x: day_of_the_week(x.date_time))
# for day, daily_meetings in weekly_meetings:
#     first_meeting = first(daily_meetings)
#     last_meeting = last(daily_meetings) if len(list(daily_meetings)) > 1 else None
#     responder_command.default_responder(response=first_meeting)
#     if last_meeting:
#         responder_command.default_responder(response=last_meeting)