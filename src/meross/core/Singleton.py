class Singleton:

    instances = {}
         
    @classmethod
    def New(cls, instance, *args, **kw) -> object:

        def _Create(*args, **kw):
            if instance not in cls.instances:
                cls.instances[instance] = instance(*args, **kw)

            return cls.instances[instance]

        return _Create

    @classmethod
    def Clean(cls, instance, *args, **kw):
        if (cls.instances[instance]):
            del cls.instances[instance]

