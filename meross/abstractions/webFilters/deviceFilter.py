from dataclasses import dataclass
from meross.abstractions.webFilters.base.BaseFilter import BaseFilter
from meross.abstractions.device.deviceModel import deviceModel
from typing import List


@dataclass
class DeviceFilter(BaseFilter):

    def __init__(self, data: str):

        self.devices: List[deviceModel]

        super(DeviceFilter, self).__init__(data, deviceModel)
        self.devices = self._parsedData

