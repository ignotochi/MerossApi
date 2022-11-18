from dataclasses import dataclass
from .BaseFilters import BaseFilter
from ..DeviceModel import DeviceModel

@dataclass
class DevicesFilter(BaseFilter):

    devices: [DeviceModel]

    def __init__(self, data: str):
        if (data != None):
            self.devices = super().__init__(data, DeviceModel)
        else:
            self.devices = []
