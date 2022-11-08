from dataclasses import dataclass
from .BaseFilters import BaseFilter
from ...abstractions import Device
from ...abstractions.ToggledDevice import ToggledDevice


@dataclass
class ToggleDeviceFilter(BaseFilter):

    toggledDevices: [ToggledDevice]

    def __init__(self, data: str = None):
        if (data != None):
           self.toggledDevices = super().__init__(data, ToggledDevice)
        else:
           self.toggledDevices = []
        
