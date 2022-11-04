class BaseFilter():

    @staticmethod
    def NormalizeArrayFilters(item: str) -> []:
        __arrayFilters = []

        __isArrayFilter = "[" in item and "]" in item

        if (__isArrayFilter):
            params: [str] = item.replace(
                '[', '').replace(']', '').replace(',', ' ').split()

            for param in params:
                __arrayFilters.append(param)
        
        return __arrayFilters
