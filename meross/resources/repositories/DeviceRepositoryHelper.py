from meross.abstractions.device.Device import Device


class LoadDeviceHelper:

    @staticmethod
    def MapDevice(item):
        outcome: Device = Device(
            deviceName=item.name,
            model=item.type,
            firmwareVersion=item.firmware_version,
            hardwareVersion=item.hardware_version,
            deviceUid=item.uuid,
            status=item.online_status.name)

        return outcome
