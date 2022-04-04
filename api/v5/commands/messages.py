from typing import Iterable, Union, Optional
from typing.generic import Contact, DateTime, Entity
from typing.message import Message, MessageContent


def create_message(
    recipient: Optional[Contact] = None, exact_content: Optional[MessageContent] = None
) -> Message:
    raise NotImplementedError
