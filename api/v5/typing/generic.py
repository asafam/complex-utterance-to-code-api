from __future__ import annotations
from abc import abstractclassmethod
from typing import Optional, List
from resolveable import Resolveable
from exceptions import NoSuchValueException
from datetime import datetime


class Entity():
    pass

class Contact(Entity, Resolveable):
    pass


class DateTime(Entity, Resolveable):
    value: datetime
    
    @classmethod
    def resolve_from_text(cls, text: str, recovered_text: Optional[List[str]] = None) -> DateTime:
        value = None # replace with actual implementation of inferring the date time from the given input text
    
        if value == None:
            raise NoSuchValueException(text=text, 
                                       recovery_prompt=f"There is no {text}. Did you mean some other date?",
                                       message=f"There is no {text}")
       
        date_time = DateTime()
        date_time.value = value     
        return date_time
            
    
    
class Location(Entity, Resolveable):
    pass