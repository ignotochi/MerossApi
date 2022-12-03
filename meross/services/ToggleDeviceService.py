from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.ToggledDevice import ToggledDevice
from meross.services.AuthService import AuthService
from typing import List, Union


class ToggleDeviceService:

    @staticmethod
    def Toggle(devices: List[ToggledDevice], token: str) -> Union[List[str], str]:
        try:
            context = AuthService.RetrieveUserContext(token)
            result = DeviceRepository.ToggleMerossDevice(context, devices)
            return result

        except Exception as exception:
            return "ToggleError: " + str(exception.args[0])
