from typing import Iterable, Optional
from typing.generic import Contact, DateTime
from typing.message import Message, MessageContent


def get_messages(
    date_time: Optional[DateTime] = None,
    exact_content: Optional[MessageContent] = None,
    sender: Optional[Contact] = None,
    recipient: Optional[Contact] = None,
) -> Iterable[Message]:
    raise NotImplementedError