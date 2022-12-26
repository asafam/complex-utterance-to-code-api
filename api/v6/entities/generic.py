
from typing import Optional, List
from entities.entity import Entity
from entities.resolvable import Resolvable
# from exceptions.exceptions import NoSuchValueException
from datetime import datetime

    

class Content(Entity, Resolvable):
    pass 


class Contact(Entity, Resolvable):
    pass


class DateTime(Entity, Resolvable):
    value: datetime
    
    # @classmethod
    # def resolve_from_text(cls, text: str, recovered_text: Optional[str] = None) -> DateTime | List[DateTime]:
    #     data = DataModel.get_data(cls)
    #     if data is None:
    #         raise NotImplementedError()
        
    #     items = [x for x in data if x.data.get('text') == text]
        
    #     if len(items) == 0:
    #         raise ValueError()
    #     else:
    #         result = items[0] if len(items) == 1 else items
    #         return result

    # @classmethod
    # def resolve_from_text(
    #     cls, 
    #     text: str, 
    #     recovered_text: Optional[List[str]] = None
    # ) -> DateTime:
    #     value = None  # replace with actual implementation of inferring the date time from the given input text

    #     if value == None:
    #         payload = {
    #             'text': text
    #         }
    #         raise NoSuchValueException(
    #             payload=payload,
    #             recovery_prompt=f"There is no {text}. Did you mean some other date?",
    #             message=f"There is no {text}",
    #         )

    #     date_time = DateTime()
    #     date_time.value = value
    #     return date_time


class Location(Entity, Resolvable):
    pass


class Amount(Entity, Resolvable):
    pass


class TimeDuration(Entity, Resolvable):
    pass
