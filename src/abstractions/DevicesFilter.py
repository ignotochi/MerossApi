from .BaseFilters import BaseFilter

class DevicesFilter(BaseFilter):
    
    devices: [str] = []
    
    def __init__(self, item: str):
        if (item):
         self.devices = super().NormalizeArrayFilters(item)

    
        
    
        
