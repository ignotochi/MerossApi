from ...core.JsonHelper import JsonUtils
from dataclass_wizard import fromlist, asdict, DateTimePattern
from typing import TypeVar, Generic, List, Tuple

T = TypeVar("T")

class BaseFilter():

    def __init__(self, data: str, obj: T) -> T:
        
        if (data):
            __parsedData: ToggleDeviceFilter = JsonUtils.ParseData(data) 
            __isArray = isinstance(__parsedData, list)

            if (__isArray):
                __dataClassObj = fromlist(obj, __parsedData)  
                items = []         
                for obj in __dataClassObj:
                    items.append(obj)              
                return items          
            
            else:
                __dataClassObj = fromlist(obj, [__parsedData])  
                return __dataClassObj[0]
            

