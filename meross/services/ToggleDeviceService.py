from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.ToggledDevice import ToggledDevice
from meross.services.AuthService import AuthService
from typing import List, Union


class ToggleDeviceService:

    @staticmethod
    def Toggle(devices: List[ToggledDevice]) -> Union[List[str], str]:
        try:
            result: List[str] = []

            context = AuthService.context

            result = DeviceRepository.ToggleMerossDevice(context, devices)

            return result

        except Exception as exception:
            return "ToggleError: " + str(exception.args[0])
