import json

class JsonUtils():

    @classmethod
    def ParseData(self, data: str) -> None:        
        __parsedData = json.loads(data) if len(json.loads(data)) != {} else None       
        return __parsedData
