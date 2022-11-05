from dataclasses import dataclass
from .BaseFilters import BaseFilter

@dataclass
class DevicesFilter(BaseFilter):

    devices: [str]
    
    def __init__(self, data: str):
        super().__init__(data)
        parsedData: DevicesFilter = super().GetParsedData()
        
        self.devices = parsedData['devices']
        
        


            
