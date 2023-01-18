from abc import abstractclassmethod
from typing import List, Optional, List, Union
from entities.generic import DateTime, Location
from entities.home import *
from providers.data_model import DataModel


class SmartHome:
    @classmethod
    def find_home_devices(
        cls,
        device_name: Optional[HomeDeviceName] = None,
    ) -> List[HomeDeviceEntity]:
        data_model = DataModel()
        data = data_model.get_data(HomeDeviceEntity)
        if device_name:
            data = [x for x in data if x.data.get("device_name") == device_name]

        return data

    @classmethod
    def execute_home_device_action(
        cls,
        start_date_time: Optional[DateTime] = None,
        end_date_time: Optional[DateTime] = None,
        device_name: Optional[HomeDeviceName] = None,
        device_action: Optional[HomeDeviceAction] = None,
        device_value: Optional[HomeDeviceValue] = None,
    ) -> List[HomeDeviceEntity]:
        data_model = DataModel()
        data = data_model.get_data(HomeDeviceEntity)
        if start_date_time:
            data = [x for x in data if x.data.get("start_date_time") == start_date_time]
            
        if end_date_time:
            data = [x for x in data if x.data.get("end_date_time") == end_date_time]

        if device_name:
            data = [x for x in data if x.data.get("device_name") == device_name]

        if device_action:
            data = [x for x in data if x.data.get("device_action") == device_action]

        if device_value:
            data = [x for x in data if x.data.get("device_value") == device_value]

        return data
