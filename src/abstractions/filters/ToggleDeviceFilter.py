from dataclasses import dataclass
from .BaseFilters import BaseFilter
from ...abstractions.ToggledDevice import ToggledDevice
from typing import List


@dataclass
class ToggleDeviceFilter(BaseFilter):

    toggledDevices: List[ToggledDevice]

    def __init__(self, data: str = None):
        if (data != None):
           self.toggledDevices = super().__init__(data, ToggledDevice)
        else:
           self.toggledDevices = []
        
