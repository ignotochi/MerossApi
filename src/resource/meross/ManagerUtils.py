from meross_iot.model.enums import OnlineStatus
from ...abstractions.DeviceType import DeviceType
from ...abstractions.Device import Device
from ...abstractions.ToggledDevice import ToggledDevice
from ...abstractions.auth import Auth
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient


class ManagerUtils():

    @staticmethod
    async def StopManagerAndLogOut(manager: MerossManager) -> None:
        manager.close()
        await manager.client.async_logout()

    @staticmethod
    async def GetDevices(manager: MerossManager, devicesType: [DeviceType]) -> [Device]:
        devices: [Device] = []

        await manager.async_device_discovery()

        for device in devicesType:
            device: DeviceType = device
            discoveredDevices = manager.find_devices(
                device_type=device.deviceType)

            if (len(discoveredDevices) > 0):
                for discoveredDevice in discoveredDevices:
                    await discoveredDevice.async_update()
                    devices.append(discoveredDevice)

        return devices

    @staticmethod
    async def ToggleDevice(manager, toggledDevice: ToggledDevice) -> str:

        deviceId: str = ""

        await manager.async_device_discovery()
        devices = manager.find_devices(toggledDevice.deviceId)

        if (len(devices) > 0):        
            await device.async_update()
            device = devices[0]
            deviceId = device.uuid

            if (toggledDevice.enabled == True):
                await device.async_turn_on(channel=0)
            else:
                await device.async_turn_off(channel=0)

        return deviceId
