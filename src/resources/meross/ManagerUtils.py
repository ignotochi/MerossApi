from ...abstractions.DeviceType import DeviceType
from ...abstractions.Device import Device
from ...abstractions.ToggledDevice import ToggledDevice
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross_iot.controller.device import BaseDevice
from ..meross.Manager import Manager
import asyncio


class ManagerUtils(Manager):

    @classmethod
    def __init__(cls, user: str, passwd: str):
        super(ManagerUtils, cls).__init__(user, passwd)

    @classmethod
    async def StopManagerAndLogOut(cls, client: MerossHttpClient) -> bool:
        cls.manager.close()
        await client.async_logout()
        return (cls.manager._http_client._cloud_creds == None)

    @classmethod
    async def GetDevices(cls, devicesType: [DeviceType]) -> [Device]:
        devices: [Device] = []

        await cls.Discover()

        for device in devicesType:
            discoveredDevices: [BaseDevice] = cls.Find(device.deviceType)

            if (discoveredDevices and len(discoveredDevices) > 0):

                for discoveredDevice in discoveredDevices:
                    await cls.Update(discoveredDevice)
                    devices.append(device)

        return devices

    @classmethod
    async def ToggleDevice(cls, toggledDevice: ToggledDevice) -> str:
        deviceId: str = None

        await cls.manager.async_device_discovery()
        devices: [BaseDevice] = cls.manager.find_devices(toggledDevice.deviceId)

        if (devices and len(devices) > 0):
            device: BaseDevice = devices[0]
            deviceId = device.uuid

            await device.async_update()

            if (toggledDevice.enabled == True):
                await device.async_turn_on(channel=0)
            else:
                await device.async_turn_off(channel=0)

        return deviceId
