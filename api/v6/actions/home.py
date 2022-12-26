from abc import abstractclassmethod
from typing import Iterable, Optional, List, Union
from entities.generic import DateTime, Location
from entities.home import *
from providers.data_model import DataModel


class SmartHome:
    @classmethod
    def find_home_devices(
        cls,
        device_name: Optional[HomeDeviceName] = None,
    ) -> Iterable[HomeDeviceEntity]:
        data_model = DataModel()
        data = data_model.get_data(HomeDeviceEntity)
        if device_name:
            data = [x for x in data if x.data.get("device_name") == device_name]

        return data

    @classmethod
    def execute_home_device_command(
        cls,
        date_time: Optional[Union[DateTime, List[DateTime]]] = None,
        device_name: Optional[HomeDeviceName] = None,
        device_value: Optional[HomeDeviceValue] = None,
    ) -> Iterable[HomeDeviceEntity]:
        data_model = DataModel()
        data = data_model.get_data(HomeDeviceEntity)
        if date_time:
            if type(date_time) == list:
                data = [x for x in data if x.data.get("date_time") in date_time]
            else:
                data = [x for x in data if x.data.get("date_time") == date_time]

        if device_name:
            data = [x for x in data if x.data.get("device_name") == device_name]

        if device_value:
            data = [x for x in data if x.data.get("device_value") == device_value]

        return data
