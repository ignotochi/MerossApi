from ...tools.JsonHelper import JsonUtils

class BaseFilter():
    
    def __init__(self, data: str) -> None:
        if (data): return JsonUtils.ParseData(data)

        



