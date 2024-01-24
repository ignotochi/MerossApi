from dataclasses import dataclass


@dataclass
class ToggledDevice:
    deviceId: str
    enabled: bool
