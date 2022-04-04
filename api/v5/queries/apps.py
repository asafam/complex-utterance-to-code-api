from typing import Iterable, Optional
from typing.generic import Contact, DateTime
from typing.apps import AppName, App


def get_apps(
    app_name: Optional[AppName] = None,
) -> Iterable[App]:
    raise NotImplementedError
