from typing import Any, Callable


class Singleton:

    instances = {}

    @classmethod
    def __new__(cls, instance, *args, **kw) -> Callable:
        return cls.Create(instance)

    @classmethod
    def Create(cls, instance, *args, **kw) -> Callable:
        if instance not in cls.instances:
            cls.instances[instance] = instance(*args, **kw)

        return cls.instances[instance]

    @classmethod
    def Clean(cls, instance, *args, **kw):
        if cls.instances[instance]:
            del cls.instances[instance]


#class Singleton:

#    instances = {}

#    @classmethod
#    def New(cls, instance, *args, **kw) -> Callable:
#        def _Create(*args, **kw):
#            if instance not in cls.instances:
#                cls.instances[instance] = instance(*args, **kw)

#            return cls.instances[instance]

#        return _Create

#    @classmethod
#    def Clean(cls, instance, *args, **kw):
#        if cls.instances[instance]:
#            del cls.instances[instance]
