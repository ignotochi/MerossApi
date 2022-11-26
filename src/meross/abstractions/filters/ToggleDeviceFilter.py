from dataclasses import dataclass
from meross.abstractions.filters.BaseFilters import BaseFilter
from meross.abstractions.ToggledDevice import ToggledDevice
from typing import List


@dataclass
class ToggleDeviceFilter(BaseFilter):
    def __init__(self, data: str = None):

        self.toggledDevices: List[ToggledDevice]

        if data != None:
            super(ToggleDeviceFilter, self).__init__(data, ToggledDevice)
            self.toggledDevices = self._parsedData
        else:
            self.toggledDevices = []
