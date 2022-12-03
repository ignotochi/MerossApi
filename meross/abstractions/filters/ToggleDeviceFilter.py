from dataclasses import dataclass
from meross.abstractions.filters.BaseFilters import BaseFilter
from meross.abstractions.ToggledDevice import ToggledDevice
from typing import List


@dataclass
class ToggleDeviceFilter(BaseFilter):
    def __init__(self, data: bytes):

        self.toggledDevices: List[ToggledDevice]

        super(ToggleDeviceFilter, self).__init__(data, ToggledDevice)
        self.toggledDevices = self._parsedData

