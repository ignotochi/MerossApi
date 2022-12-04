from dataclasses import dataclass
from meross.abstractions.webFilters.base.BaseFilters import BaseFilter
from meross.abstractions.device.ToggledDevice import ToggledDevice
from typing import List


@dataclass
class ToggleDeviceFilter(BaseFilter):
    def __init__(self, data: bytes):

        self.toggledDevices: List[ToggledDevice]

        super(ToggleDeviceFilter, self).__init__(data, ToggledDevice)
        self.toggledDevices = self._parsedData

