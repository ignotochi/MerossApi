from ...abstractions.DeviceType import DeviceType
from ...abstractions.Device import Device
from ...abstractions.ToggledDevice import ToggledDevice
from ...abstractions.auth import Auth
from meross_iot.manager import MerossManager
from meross_iot.http_api import MerossHttpClient
from meross_iot.controller.device import BaseDevice
from ...context.context import Context


class ManagerUtils():

    @staticmethod
    async def StopManagerAndLogOut(manager: MerossManager, client: MerossHttpClient) -> bool:
        manager.close()
        await client.async_logout()
        return (manager._http_client._cloud_creds == None)

    @staticmethod
    async def GetDevices(context: Context, devicesType: [DeviceType]) -> [Device]:
        devices: [Device] = []
        
        manager = context.managerTools.manager
        
        await manager.async_device_discovery()

        for device in devicesType:
            device: DeviceType = device
            discoveredDevices: [BaseDevice] = manager.find_devices(device_type=device.deviceType)

            if (discoveredDevices and len(discoveredDevices) > 0):
                
                for discoveredDevice in discoveredDevices:    
                    device: BaseDevice = discoveredDevice
                    
                    await device.async_update()
                    devices.append(device)

        return devices

    @staticmethod
    async def ToggleDevice(context: Context, toggledDevice: ToggledDevice) -> str:

        deviceId: str = None
        
        manager = context.managerTools.manager 
        
        await manager.async_device_discovery()
        
        devices: [BaseDevice] = manager.find_devices(toggledDevice.deviceId)

        if (devices and len(devices) > 0):        
            
            device: BaseDevice = devices[0]
            deviceId = device.uuid 
            
            await device.async_update()
            
            if (toggledDevice.enabled == True):
                await device.async_turn_on(channel=0)
            else:
                await device.async_turn_off(channel=0)

        return deviceId
