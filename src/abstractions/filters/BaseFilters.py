from ...tools.JsonHelper import JsonUtils
from dataclass_wizard import fromlist, asdict, DateTimePattern

class BaseFilter():

    def __init__(self, data: str, obj: type) -> object:
        
        if (data):
            __parsedData: ToggleDeviceFilter = JsonUtils.ParseData(data) 
            __dataClassObj = fromlist(obj, __parsedData)
            __isArray = isinstance(__parsedData, list)  

            if (__isArray):
                items = []         
                for obj in __dataClassObj:
                    items.append(obj)              
                return items          
            
            else:
                return __dataClassObj
            

