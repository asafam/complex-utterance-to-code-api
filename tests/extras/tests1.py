from entities.generic import *
from entities.events import *
from entities.message import *
from entities.music import *
from entities.navigation import *
from entities.reminder import *
from entities.shopping import *
from entities.weather import *
from actions.calendar import Calendar
from actions.clock import *
from actions.events import *
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


def test_e0():
    """
    Send Tyler a text saying hi and send one to Susan too.
    """
    # test data
    data_model = DataModel(reset=True)
    data_contact1 = Contact(text="Tyler", value="Tyler")
    data_model.append(data_contact1)
    data_contact2 = Contact(text="Susan", value="Susan")
    data_model.append(data_contact2)
    data_content = Content(text="hi", value="hi")
    data_model.append(data_content)

    # code block to test
    recipient = Contact.resolve_from_text("Tyler")
    content = Content.resolve_from_text("hi")
    Messages.send_message(recipient=recipient, content=content)

    recipient = Contact.resolve_from_text("Susan")
    Messages.send_message(recipient=recipient, content=content)

    # assertions
    data_messages_lists = data_model.get_response([MessageEntity])
    assert len(data_messages_lists) == 2
    data_message1 = data_messages_lists[0]
    assert data_message1.data.get("recipient") == data_contact1
    assert data_message1.data.get("content") == data_content
    data_message2 = data_messages_lists[1]
    assert data_message2.data.get("recipient") == data_contact2
    assert data_message2.data.get("content") == data_content
