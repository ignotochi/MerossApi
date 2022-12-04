from abc import ABC
from meross.abstractions.context.IContext import IContext
from meross.abstractions.device.DeviceModel import DeviceModel
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross.abstractions.device.Device import Device
from typing import List


class IDeviceRepository(ABC, object):

    @staticmethod
    def LoadMerossDevices(context: IContext, devices: List[DeviceModel]) -> List[Device]:
        pass

    @staticmethod
    def ToggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[str]:
        pass
