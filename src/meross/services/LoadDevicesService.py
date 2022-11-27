from meross.resources.repositories.DeviceRepository import DeviceRepository
from meross.abstractions.Device import Device
from meross.abstractions.DeviceModel import DeviceModel
from meross.resources.repositories.DeviceRepositoryHelper import LoadDeviceHelper
from meross.services.AuthService import AuthService
from typing import List, Union


class LoadDevicesService:

    @staticmethod
    def Load(devices: List[DeviceModel]) -> Union[List[Device] , str]: 
        try:
            result: List[Device] = []

            context = AuthService.context
            
            items = DeviceRepository.LoadMerossDevices(context, devices)

            if (items and len(items) > 0):
                for item in items:
                    outcome = LoadDeviceHelper.MapDevice(item)
                    result.append(outcome)
            
            return result
                    
        except Exception as exception:
            return "LoadError: " + str(exception.args[0])
