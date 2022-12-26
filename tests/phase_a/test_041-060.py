from entities.generic import *
from entities.events import *
from entities.home import *
from entities.message import *
from entities.music import *
from entities.navigation import *
from entities.reminder import *
from entities.shopping import *
from entities.weather import *
from actions.calendar import Calendar
from actions.clock import *
from actions.events import *
from actions.home import *
from actions.messages import Messages
from actions.music import Music
from actions.navigation import Navigation
from actions.reminders import Reminders
from actions.responder import Responder
from actions.shopping import Shopping
from actions.weather import Weather
from providers.data_model import DataModel
from datetime import datetime, timedelta
import utils


def test41():
    """
    Set a reminder at 3:00 PM that I will need to pick up my items from the store, and text Jason to meet me at the store at 2:50 PM.
    """
    # test data
    data_model = DataModel(reset=True)
    data_date_time = DateTime(
        text="at 3 PM", value=datetime.now.replace(hour=15, minute=0)
    )
    data_model.append(data_date_time)
    data_content = Content(
        text="I will need to pick up my items from the store",
        value="I will need to pick up my items from the store",
    )
    data_model.append(data_content)
    data_recipient = Contact(text="Jason", value="Jason Smith")
    data_model.append(data_recipient)
    data_content_message = Content(
        text="meet me at the store at 2:50 PM", value="meet me at the store at 2:50 PM"
    )
    data_model.append(data_content_message)

    # assertions
    data_reminders = data_model.get_data(ReminderEntity)
    assert len(data_reminders) == 1
    data_reminder = data_reminders[0]
    assert data_reminder.data.get("date_time") == data_date_time
    assert data_reminder.data.get("content") == data_content

    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content_message


def test42():
    """
    Add entry in the calendar for a lunch meeting with Jack tomorrow at 3 PM, also text Jack that we will be meeting at 3 PM for lunch.
    """
    # test data
    data_model = DataModel(reset=True)
    data_date_time = DateTime(
        text="tomorrow at 3 PM",
        value=(datetime.now() + timedelta(days=1)).replace(hour=15, minute=0),
    )
    data_model.append(data_date_time)
    data_event_name = EventName(
        text="lunch meeting with Jack", value="lunch meeting with Jack"
    )
    data_model.append(data_event_name)
    data_recipient = Contact(text="Jack", value="Jack Smith")
    data_model.append(data_recipient)
    data_content_message = Content(
        text="we will be meeting at 3 PM for lunch",
        value="we will be meeting at 3 PM for lunch",
    )
    data_model.append(data_content_message)

    # assertions
    data_events = data_model.get_data(EventEntity)
    assert len(data_events) == 1
    data_event = data_events[0]
    assert data_event.data.get("date_time") == data_date_time
    assert data_event.data.get("event_name") == data_event_name

    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content_message


def test43():
    """
    Set the thermostat to 70 degrees and play my romantic playlist.
    """
    # test data
    data_model = DataModel(reset=True)
    data_home_device_name = HomeDeviceName(text="the thermostat", value="thermostat")
    data_model.append(data_home_device_name)
    data_home_device_value = HomeDeviceValue(text="70 degrees", value=70)
    data_model.append(data_home_device_value)
    data_playlist = Playlist(text="my romantic playlist", value="my romantic playlist")
    data_model.append(data_playlist)

    # assertions
    data_home_devices = data_model.get_data(HomeDeviceEntity)
    assert len(data_home_devices) == 1
    data_home_device = data_home_devices[0]
    assert data_home_device.data.get("device_name") == data_home_device_name
    assert data_home_device.data.get("device_value") == data_home_device_value

    data_musics = data_model.get_data(MusicEntity)
    assert len(data_musics) == 1
    data_music = data_musics[0]
    assert data_music.data.get("playlist") == data_playlist


def test44():
    """
    Remind me to send an email to Mom and Dad tomorrow and delete the appointment in my calendar for Tuesday.
    """
    # test data
    data_model = DataModel(reset=True)
    data_content = Content(
        text="send an email to Mom and Dad", value="send an email to Mom and Dad"
    )
    data_model.append(data_content)
    data_date_time_tomorrow = DateTime(
        text="tomorrow",
        value=datetime.now() + timedelta(days=1),
    )
    data_model.append(data_date_time_tomorrow)
    data_date_time = DateTime(
        text="Tuesday",
        value=datetime.now() + timedelta(days=((7 + 2 - datetime.now().weekday()) % 7)),
    )
    data_model.append(data_date_time)
    data_calendar = EventCalendar(text="my calendar", value="my calendar")
    data_model.append(data_calendar)
    data_model.append(EventEntity(date_time=data_date_time))

    # assertions
    data_reminders = data_model.get_data(ReminderEntity)
    assert len(data_reminders) == 1
    data_reminder = data_reminders[0]
    assert data_reminder.data.get("date_time") == data_date_time_tomorrow
    assert data_reminder.data.get("content") == data_content

    data_events = data_model.get_data(EventEntity)
    assert len(data_events) == 0


def test45_a():
    """
    If Walmart has Jurassic World on bluray, buy it so I can pick it up tomorrow morning.
    """
    # test data
    data_model = DataModel(reset=True)
    data_store = Location(text="Walmart", value="Walmart")
    data_model.append(data_store)
    data_product = Product(
        text="Jurassic World on bluray", value="Jurassic World on bluray"
    )
    data_model.append(data_product)
    data_model.append(ProductEntity(location=data_store, product=data_product))

    # assertions
    data_orders = data_model.get_data(OrderEntity)
    assert len(data_orders) == 1
    data_order = data_orders[0]
    assert data_order.data.get("location") == data_store
    assert data_order.data.get("product") == data_product


def test45_b():
    """
    If Walmart has Jurassic World on bluray, buy it so I can pick it up tomorrow morning.
    """
    # test data
    data_model = DataModel(reset=True)
    data_store = Location(text="Walmart", value="Walmart")
    data_model.append(data_store)
    data_product = Product(
        text="Jurassic World on bluray", value="Jurassic World on bluray"
    )
    data_model.append(data_product)

    # assertions
    data_orders = data_model.get_data(OrderEntity)
    assert len(data_orders) == 0


def test46():
    """
    Get directions to Portland, and tell me if it will snow along the route in the next hour
    """
    # test data
    data_model = DataModel(reset=True)
    data_destination = Location(text="Portland", value="Portland")
    data_model.append(data_destination)
    data_direction = NavigationDirectionEntity(destination=data_destination)
    data_model.append(data_direction)
    data_weather_attribute = WeatherAttribute(text="snow", value="snow")
    data_model.append(data_weather_attribute)
    data_location = Location(text="along the route", value=data_direction)
    data_model.append(data_location)
    data_date_time = DateTime(
        text="in the next hour",
        value=datetime.now() + timedelta(hours=1),
    )
    data_model.append(data_date_time)
    data_model.append(
        WeatherForecastEntity(
            location=data_location,
            weather_attribute=data_weather_attribute,
            date_time=data_date_time,
        )
    )

    # assertions
    data_navigation_directions = data_model.get_data(NavigationDirectionEntity)
    assert len(data_navigation_directions) == 1
    data_navigation_direction = data_navigation_directions[0]
    assert data_navigation_direction.data.get("destination") == data_destination

    data_weather_forecasts_list = data_model.get_data(WeatherForecastEntity)
    assert len(data_weather_forecasts_list) == 1
    data_weather_forecasts = data_weather_forecasts_list[0]
    assert (
        data_weather_forecasts[0].data.get("weather_attribute")
        == data_weather_attribute
    )
    assert data_weather_forecasts[0].data.get("location") == data_location
    assert data_weather_forecasts[0].data.get("date_time") == data_date_time


def test47_a():
    """
    Check the weather and text Mike that I will meet them later if it's hot.
    """
    # test data
    data_model = DataModel(reset=True)
    data_weather_attribute = WeatherAttribute(text="hot", value="hot")
    data_model.append(data_weather_attribute)
    data_model.append(WeatherForecastEntity(weather_attribute=data_weather_attribute))
    data_recipient = Contact(text="Mike", value="Mike Miller")
    data_model.append(data_recipient)
    data_content = Content(
        text="I will meet them later", value="I will meet them later"
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content


def test47_b():
    """
    Check the weather and text Mike that I will meet them later if it's hot.
    """
    # test data
    data_model = DataModel(reset=True)
    data_weather_attribute = WeatherAttribute(text="cold", value="cold")
    data_model.append(data_weather_attribute)
    data_model.append(WeatherForecastEntity(weather_attribute=data_weather_attribute))
    data_recipient = Contact(text="Mike", value="Mike Miller")
    data_model.append(data_recipient)
    data_content = Content(
        text="I will meet them later", value="I will meet them later"
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 0


def test48():
    """
    Add milk to the shopping list and text my brother that he needs to look at the updated shopping list.
    """
    pass


def test49():
    """
    Add toilet paper to my Amazon weekend shopping list and text a link of the list to Diana.
    """
    # test data
    data_model = DataModel(reset=True)
    data_product = Product(text="eggs", value="eggs")
    data_model.append(data_product)
    data_model.append(ShoppingListEntity(products=[data_product]))
    data_recipient = Contact(text="Steve", value="Steven Smith")
    data_model.append(data_recipient)
    data_content = Content(
        text="please buy eggs at the grocery store",
        value="please buy eggs at the grocery store",
    )
    data_model.append(data_content)

    # assertions
    data_shopping_lists = data_model.get_data(ShoppingListEntity)
    assert len(data_shopping_lists) == 1
    data_shopping_list = data_shopping_lists[0]
    assert data_shopping_list.data.get("products").index(data_product) >= 0

    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content


def test50_a():
    """
    If the weather is going to be sunny Saturday morning, send an email to Ashley asking if she wants to go for a hike.
    Send a message to my friends list on Monday telling them to remember to vote and set a reminder to me to remember to vote.
    Show me all of the musical events within 10 miles of me.
    Play my favorite music playlist and tell John I am running late and will be there soon.
    Look up current prices for Chicago Blackhawks tickets for tomorrow's game and tell me what the traffic conditions will be like around 5 PM
    Set timer to 30 mins and remind me to take the fish out of the oven.
    Check the weather and if it's above 80 degrees, set a reminder on my calendar for "Go to the park later"
    Remind me on Sunday about my doctor's appointment next Monday and give me directions to the doctor's office.
    For Shakey Graves' upcoming summer tour, what will be the closest show to me and how many miles away is the venue?
    If is is raining at 8pm turn the heat up 5 degrees.
    If I get a text message from my boss Tony, then check my mail to see if I have any emails from work.
    """
    # test data
    data_model = DataModel(reset=True)
    data_sender = Contact(text="Ruby", value="Ruby Chen")
    data_model.append(data_sender)
    data_contact = Contact(text="Steve", value="Steven Smith")
    data_model.append(data_contact)
    data_date_time = DateTime(text="tonight", value=datetime.now())
    data_model.append(data_date_time)
    data_date_time_tomorrow = DateTime(
        text="tomorrow", value=datetime.now() + timedelta(days=1)
    )
    data_model.append(data_date_time_tomorrow)
    data_model.append(MessageEntity(sender=data_sender, date_time=data_date_time))
    data_model.append(
        MessageEntity(sender=data_sender, date_time=data_date_time_tomorrow)
    )
    data_model.append(MessageEntity(sender=data_contact, date_time=data_date_time))
    data_alarm_date_time = DateTime(text="7am", value="7am")
    data_model.append(data_alarm_date_time)
    data_model.append(AlarmEntity(date_time=data_alarm_date_time))

    # assertions
    data_alarms = data_model.get_data(AlarmEntity)
    assert len(data_alarms) == 1
    data_alarm = data_alarms[0]
    assert data_alarm.data.get("date_time") == data_alarm_date_time


def test50_b():
    """
    If I receive a text from Ruby tonight, change my alarm to 7am.
    """
    # test data
    data_model = DataModel(reset=True)
    data_sender = Contact(text="Ruby", value="Ruby Chen")
    data_model.append(data_sender)
    data_contact = Contact(text="Steve", value="Steven Smith")
    data_model.append(data_contact)
    data_date_time = DateTime(text="tonight", value=datetime.now())
    data_model.append(data_date_time)
    data_date_time_tomorrow = DateTime(
        text="tomorrow", value=datetime.now() + timedelta(days=1)
    )
    data_model.append(data_date_time_tomorrow)
    data_model.append(
        MessageEntity(sender=data_sender, date_time=data_date_time_tomorrow)
    )
    data_model.append(MessageEntity(sender=data_contact, date_time=data_date_time))
    data_alarm_date_time_7 = DateTime(text="7am", value="7am")
    data_model.append(data_alarm_date_time_7)
    data_alarm_date_time_9 = DateTime(text="9am", value="9am")
    data_model.append(data_alarm_date_time_9)
    data_model.append(AlarmEntity(date_time=data_alarm_date_time_9))

    # assertions
    data_alarms = data_model.get_data(AlarmEntity)
    assert len(data_alarms) == 1
    data_alarm = data_alarms[0]
    assert data_alarm.data.get("date_time") != data_alarm_date_time


def test51():
    """ """
    pass


def test52():
    """ """
    pass


def test53():
    """ """
    pass


def test54():
    """ """
    pass


def test55():
    """ """
    pass


def test56():
    """ """
    pass


def test57():
    """ """
    pass


def test59():
    """ """
    pass


def test60():
    """ """
    pass
