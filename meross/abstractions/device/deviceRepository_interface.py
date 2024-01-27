from abc import ABC
from meross.abstractions.context.context_interface import IContext
from meross.abstractions.device.deviceModel import deviceModel
from meross.abstractions.device.toggledDevice import ToggledDevice
from meross.abstractions.device.device import device
from typing import List


class IDeviceRepository(ABC, object):

    @staticmethod
    def loadMerossDevices(context: IContext, devices: List[deviceModel]) -> List[device]:
        pass

    @staticmethod
    def toggleMerossDevice(context: IContext, devices: List[ToggledDevice]) -> List[str]:
        pass
