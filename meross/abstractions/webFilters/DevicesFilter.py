from dataclasses import dataclass
from meross.abstractions.webFilters.base.BaseFilters import BaseFilter
from meross.abstractions.device.DeviceModel import DeviceModel
from typing import List


@dataclass
class DevicesFilter(BaseFilter):

    def __init__(self, data: bytes):

        self.devices: List[DeviceModel]

        super(DevicesFilter, self).__init__(data, DeviceModel)
        self.devices = self._parsedData

