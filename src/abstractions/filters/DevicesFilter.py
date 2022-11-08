from dataclasses import dataclass
from .BaseFilters import BaseFilter

@dataclass
class DevicesFilter(BaseFilter):

    devices: [str]
    
    def __init__(self, data: str):
        self.devices = []
        parsedData: DevicesFilter = super().__init__(data)
        
        if (parsedData):
         self.devices = parsedData['devices']
        
        


            
