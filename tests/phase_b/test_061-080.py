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


def test61():
    """
    Set alarm for 6 AM and set the bedroom lights to turn on at 6 AM.
    """
    # test data
    data_model = DataModel(reset=True)
    data_date_time = DateTime(text="6 AM", value="6 AM")
    data_model.append(data_date_time)
    data_device = Device(text="the bedroom lights", value="the bedroom lights")
    data_model.append(data_device)
    data_device_status = DeviceStatus(text="turn on", value="turn on")
    data_model.append(data_device_status)
    data_date_time2 = DateTime(text="at 6 AM", value="at 6 AM")
    data_model.append(data_date_time2)

    # assertions
    data_alarms = data_model.get_data(AlarmEntity)
    assert len(data_alarms) == 1
    data_alarm = data_alarms[0]
    assert data_alarm.data.get("date_time") == data_date_time

    data_alarms = data_model.get_data(HomeDeviceEntity)
    assert len(data_alarms) == 1
    data_alarm = data_alarms[0]
    assert data_alarm.data.get("device") == data_device
    assert data_alarm.data.get("status") == data_device_status
    assert data_alarm.data.get("date_time") == data_date_time2


def test62():
    """
    Message Alex and ask who that opening act was at the concert last night and then add songs from that artist to my playlist.
    """
    pass


def test63_a():
    """
    If the weather is nice tomorrow, text Jenny if she would like to go to the park
    """
    # test data
    data_model = DataModel(reset=True)
    data_weather_attribute = WeatherAttribute(text="nice", value="nice")
    data_model.append(data_weather_attribute)
    data_date_time = DateTime(text="tomorrow", value="tomorrow")
    data_model.append(data_date_time)
    data_model.append(
        WeatherForecastEntity(
            date_time=data_date_time, weather_attribute=data_weather_attribute
        )
    )
    data_recipient = Contact(text="Jenny", value="Jennifer Lopez")
    data_model.append(data_recipient)
    data_content = Content(
        text="if she would like to go to the park",
        value="if she would like to go to the park",
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content


def test63_b():
    """
    If the weather is nice tomorrow, text Jenny if she would like to go to the park
    """
    # test data
    data_model = DataModel(reset=True)
    data_weather_attribute = WeatherAttribute(text="nice", value="nice")
    data_model.append(data_weather_attribute)
    data_weather_attribute_neg = WeatherAttribute(text="stormy", value="storm")
    data_model.append(data_weather_attribute_neg)
    data_date_time = DateTime(text="tomorrow", value="tomorrow")
    data_model.append(data_date_time)
    data_model.append(
        WeatherForecastEntity(
            date_time=data_date_time, weather_attribute=data_weather_attribute_neg
        )
    )
    data_recipient = Contact(text="Jenny", value="Jennifer Lopez")
    data_model.append(data_recipient)
    data_content = Content(
        text="if she would like to go to the park",
        value="if she would like to go to the park",
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 0


def test64():
    """
    Send Tyler a text saying hi and send one to Susan too.
    """
    # test data
    data_model = DataModel(reset=True)
    data_tyler = Contact(text="Tyler", value="Tyler Durden")
    data_model.append(data_tyler)
    data_susan = Contact(text="Susan", value="Susan Sarandon")
    data_model.append(data_susan)
    data_content = Content(
        text="hi",
        value="hi",
    )
    data_model.append(data_content)

    # assertions
    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 2
    assert data_messages[0].data.get("recipient") == data_tyler
    assert data_messages[0].data.get("content") == data_content
    assert data_messages[1].data.get("recipient") == data_susan
    assert data_messages[1].data.get("content") == data_content


def test65():
    """
    If I go out shopping at the grocery store later today please lock the doors behind me and shut off the AC.
    """
    pass


def test66():
    """
    Set timer for one hour labeled workout and start playing my music playlist titled workout tunes.
    """
    # test data
    data_model = DataModel(reset=True)
    data_duration = DateTime(text="one hour", value=datetime.timedelta(hours=1))
    data_model.append(data_duration)
    data_playlist = Playlist(text="workout tunes", value="workout tunes")
    data_model.append(data_playlist)
    data_model.append(MusicEntity(playlist=data_playlist))

    # assertions
    data_timers = data_model.get_data(TimerEntity)
    assert len(data_timers) == 1
    data_time = data_timers[0]
    assert data_time.data.get("duration") == data_duration

    data_music_lists = data_model.get_data(MusicEntity)
    assert len(data_music_lists) == 1
    data_music = data_music_lists[0]
    assert data_music.data.get("playlist") == data_playlist


def test67():
    """
    Turn on the living room lights and navigate Home.
    """
    # test data
    data_model = DataModel(reset=True)
    data_device_status = DeviceStatus(text="on", value="on")
    data_model.append(data_device_status)
    data_device = Device(text="the living room lights", value="the living room lights")
    data_model.append(data_device)
    data_destination = Location(text="Home", value="Home")
    data_model.append(data_destination)
    data_model.append(NavigationDirectionEntity(destination=data_destination))

    # assertions
    data_home_devices = data_model.get_data(HomeDeviceEntity)
    assert len(data_home_devices) == 1
    data_home_device = data_home_devices[0]
    assert data_home_device.data.get("device") == data_device
    assert data_home_device.data.get("device_status") == data_device_status

    data_navigation_directions_lists = data_model.get_data(NavigationDirectionEntity)
    assert len(data_navigation_directions_lists) == 1
    data_navigation_directions = data_navigation_directions_lists[0]
    assert data_navigation_directions[0].data.get("destination") == data_destination


def test68():
    """
    Look up directions to the Sushi House and text my mom, telling her that I'm leaving soon
    """
    # test data
    data_model = DataModel(reset=True)
    data_destination = Location(text="the Sushi House", value="the Sushi House")
    data_model.append(data_destination)
    data_model.append(NavigationDirectionEntity(destination=data_destination))
    data_recipient = Contact(text="my mom", value="my mom")
    data_model.append(data_recipient)
    data_content = Content(text="I'm leaving soon", value="I'm leaving soon")
    data_model.append(data_content)

    # assertions
    data_navigation_directions_lists = data_model.get_data(NavigationDirectionEntity)
    assert len(data_navigation_directions_lists) == 1
    data_navigation_directions = data_navigation_directions_lists[0]
    assert data_navigation_directions[0].data.get("destination") == data_destination

    data_messages = data_model.get_data(MessageEntity)
    assert len(data_messages) == 1
    data_message = data_messages[0]
    assert data_message.data.get("recipient") == data_recipient
    assert data_message.data.get("content") == data_content


def test69():
    """ 
    Add eggs to my shopping list and text Steve to please buy eggs at the grocery store.
    """
    # test data
    data_model = DataModel(reset=True)
    data_product = Product(text="eggs", value="eggs")
    data_model.append(data_product)
    data_model.append(ShoppingListEntity(products=[data_product]))
    data_recipient = Contact(text="Steve", value="Steven Smith")
    data_model.append(data_recipient)
    data_content = Content(text="please buy eggs at the grocery store", value="please buy eggs at the grocery store")
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


def test70_a():
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
    data_date_time_tomorrow = DateTime(text="tomorrow", value=datetime.now() + timedelta(days=1))
    data_model.append(data_date_time_tomorrow)
    data_model.append(MessageEntity(sender=data_sender, date_time=data_date_time))
    data_model.append(MessageEntity(sender=data_sender, date_time=data_date_time_tomorrow))
    data_model.append(MessageEntity(sender=data_contact, date_time=data_date_time))
    data_alarm_date_time = DateTime(text="7am", value="7am")
    data_model.append(data_alarm_date_time)
    data_model.append(AlarmEntity(date_time=data_alarm_date_time))

    # assertions
    data_alarms = data_model.get_data(AlarmEntity)
    assert len(data_alarms) == 1
    data_alarm = data_alarms[0]
    assert data_alarm.data.get("date_time") == data_alarm_date_time


def test70_b():
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
    data_date_time_tomorrow = DateTime(text="tomorrow", value=datetime.now() + timedelta(days=1))
    data_model.append(data_date_time_tomorrow)
    data_model.append(MessageEntity(sender=data_sender, date_time=data_date_time_tomorrow))
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


def test71():
    """ """
    pass


def test72():
    """ """
    pass


def test73():
    """ """
    pass


def test74():
    """ """
    pass


def test75():
    """ """
    pass


def test76():
    """ """
    pass


def test77():
    """ """
    pass


def test79():
    """ """
    pass


def test80():
    """ """
    pass
