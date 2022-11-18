from ...abstractions.DeviceModel import DeviceModel
from ...abstractions.Device import Device
from ...abstractions.ToggledDevice import ToggledDevice
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross_iot.controller.device import BaseDevice

class ManagerUtils():

    @staticmethod
    async def StopManagerAndLogOut(manager: MerossManager, client: MerossHttpClient) -> bool:
        manager.close()
        await ManagerUtils.client.async_logout()
        return (ManagerUtils.manager._http_client._cloud_creds == None)

    @staticmethod
    async def GetDevices(manager: MerossManager, devices: [DeviceModel]) -> [Device]:
        
        result: [Device] = []
        await manager.async_device_discovery()

        for device in devices:
            discoveredDevices = manager.find_devices(device_type=device.model)

            if (discoveredDevices and len(discoveredDevices) > 0):
                
                for discoveredDevice in discoveredDevices:
                    await discoveredDevice.async_update(self)
                    devices.append(discoveredDevice)

        return result

    @staticmethod
    async def ToggleDevice(manager: MerossManager, toggledDevice: ToggledDevice) -> str:
        
        deviceId: str = None

        await manager.async_device_discovery()
        device = manager.find_devices(toggledDevice.deviceId)[0]
        deviceId = device.uuid

        await device.async_update()

        if (toggledDevice.enabled == True):
            await device.async_turn_on(channel=0)
        else:
            await device.async_turn_off(channel=0)

        return deviceId
