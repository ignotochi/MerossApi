from dataclasses import dataclass
from merossApi.abstractions.filters.BaseFilters import BaseFilter
from merossApi.abstractions.ToggledDevice import ToggledDevice
from typing import List


@dataclass
class ToggleDeviceFilter(BaseFilter):

    def __init__(self, data: str = None):
        self.toggledDevices: List[ToggledDevice]

        if (data != None):
           self.toggledDevices = super().__init__(data, ToggledDevice)
        else:
           self.toggledDevices = []
        
