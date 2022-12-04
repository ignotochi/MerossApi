from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.device.ToggledDevice import ToggledDevice
from meross.abstractions.context.IContext import IContext
from typing import List, Union


class ToggleDeviceService:

    @staticmethod
    def Toggle(devices: List[ToggledDevice], context: IContext) -> Union[List[str], str]:
        try:
            result = DeviceRepository.ToggleMerossDevice(context, devices)
            return result

        except Exception as exception:
            return "ToggleError: " + str(exception.args[0])
