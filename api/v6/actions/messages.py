from abc import abstractclassmethod
from typing import Iterable, Union, Optional
from api.v6.entities.resolvable import Resolvable
from entities.generic import *
from entities.message import *
from entities.app import App


class Messages(Resolvable):
    @abstractclassmethod
    def find_messages(
        cls,
        date_time: Optional[DateTime],
        sender: Optional[Contact],
        recipient: Optional[Contact],
        content: Optional[Content],
        message_status: Optional[MessageStatus],
        message_content_type: Optional[MessageContentType],
        app: Optional[App],
    ) -> List[MessageEntity]:
        raise NotImplementedError

    @abstractclassmethod
    def send_message(
        cls, recipient: Contact, content: Content, date_time: Optional[DateTime] = None
    ) -> MessageEntity:
        raise NotImplementedError

    @abstractclassmethod
    def delete_messages(
        cls, messages: Union[MessageEntity, Iterable[MessageEntity]]
    ) -> None:
        raise NotImplementedError
