from dataclasses import dataclass
from merossApi.abstractions.filters.BaseFilters import BaseFilter
from merossApi.abstractions.DeviceModel import DeviceModel
from typing import List


@dataclass
class DevicesFilter(BaseFilter):

    devices = None

    def __init__(self, data: str):
        if (data != None):
            self.devices = super().__init__(data, DeviceModel)
        else:
            self.devices = List[DeviceModel]()