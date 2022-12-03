from typing import Callable, Dict, TypeVar
from meross.abstractions.IContext import IContext
from meross.context.Context import Context
from meross.tools.PyDictionary import PyDictionary

T = TypeVar("T")


class Singleton:
    instances: PyDictionary = PyDictionary()

    @classmethod
    def New(cls, instance: T) -> T:

        def Create(*args, **kw) -> T:

            if issubclass(instance, IContext):
                token = args[0] if args[0] is not None else None

                if token:
                    instanceExist = cls.instances.Exist(token + '_' + instance.__name__)
                else:
                    instanceExist = False

                if instanceExist is False:
                    newInstance: IContext = instance(*args, **kw)
                    dictionaryKey = newInstance.token + '_' + instance.__name__

                    cls.instances.Add(dictionaryKey, newInstance)

                    if isinstance(newInstance, Context) and cls.instances.Exist(dictionaryKey):
                        return newInstance

                else:
                    return cls.instances.Get(token + '_' + instance.__name__)

            else:
                if cls.instances.Exist(instance.__name__) is False:
                    genericInstance: T = instance(*args, **kw)
                    cls.instances.Add(instance.__name__, genericInstance)
                    return genericInstance

                else:
                    return cls.instances.Get(instance.__name__)

        return Create

    @classmethod
    def Clean(cls, instance, *args, **kw):
        cachedInstance = cls.instances.Get(instance.__name__)

        if cachedInstance:
            cls.instances.Delete(instance.__name__)
