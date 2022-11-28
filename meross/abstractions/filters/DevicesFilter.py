from dataclasses import dataclass
from meross.abstractions.filters.BaseFilters import BaseFilter
from meross.abstractions.DeviceModel import DeviceModel
from typing import List


@dataclass
class DevicesFilter(BaseFilter):

    def __init__(self, data: str):
        
        self.devices: List[DeviceModel]
        
        if (data != None):
            super(DevicesFilter, self).__init__(data, DeviceModel)
            self.devices = self._parsedData
        else:
            self.devices = List[DeviceModel]()