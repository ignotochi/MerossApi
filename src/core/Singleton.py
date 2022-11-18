@staticmethod
def Singleton(cls, *args, **kw):
     instances = {}
     
     def _singleton(*args, **kw):
        if cls not in instances:
             instances[cls] = cls(*args, **kw)
        
        return instances[cls]
     
     return _singleton