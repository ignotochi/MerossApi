from dataclasses import dataclass
from .BaseFilters import BaseFilter
from ..DeviceType import DeviceType


@dataclass
class DevicesFilter(BaseFilter):

    devices: [DeviceType]

    def __init__(self, data: str):
        if (data != None):
            self.devices = super().__init__(data, DeviceType)
        else:
            self.devices = []
