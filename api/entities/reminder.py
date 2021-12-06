from __future__ import annotations
from entities.entity import Entity


class Reminder(Entity):
    
    def call(self, funcName: str, params: dict[str, str]) -> any:
        if funcName == "foo":
            return self._foo(params)
        elif funcName == "bar":
            return self._bar(params)
        else:
            super.call(funcName, params)

    def compare(self, entity: Reminder) -> bool:
        pass
    
    def _foo(self):
        pass
    
    def _bar(self):
        pass