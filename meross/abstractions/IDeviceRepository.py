from abc import ABC, abstractmethod
from meross.abstractions.IContext import IContext
from meross.abstractions.DeviceModel import DeviceModel
from meross.abstractions.ToggledDevice import ToggledDevice
from meross.abstractions.Device import Device
from typing import List


class IDeviceRepository(ABC, object):

    @staticmethod
    def LoadMerossDevices(context: IContext, devices: List[DeviceModel]) -> List[Device]:
        pass

    @staticmethod
    def ToggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[str]:
        pass
