from dataclasses import dataclass
from .BaseFilters import BaseFilter
from ...abstractions import Device
from ...abstractions.ToggledDevice import ToggledDevice


@dataclass
class ToggleDeviceFilter(BaseFilter):

    toggledDevices: [ToggledDevice]

    def __init__(self, data: str):
        self.toggledDevices = []
        parsedData: ToggleDeviceFilter = super().__init__(data)
        __isArray = isinstance(parsedData, list)

        if (parsedData and __isArray):
            for data in parsedData:
                item = ToggledDevice()
                item.deviceId = data['deviceId']
                item.enabled = data['enabled']

                self.toggledDevices.append(item)
