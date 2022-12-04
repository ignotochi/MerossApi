from meross.tools.PyDictionary import PyDictionary
from meross.abstractions.context.IContext import IContext
from typing import TypeVar, List, Callable

T = TypeVar("T")


class SingletonHelper:

    @staticmethod
    def InitializeContext(instances: PyDictionary, instance: Callable, *args) -> IContext:

        token: str = args[0] if args[0] is not None else None

        if token:
            instanceExist = instances.Exist(token + '_' + instance.__name__)
        else:
            instanceExist = False

        if instanceExist is False:
            newInstance: IContext = instance(*args)
            dictionaryKey = newInstance.token + '_' + instance.__name__

            instances.Add(dictionaryKey, newInstance)

            if instances.Exist(dictionaryKey):
                return newInstance

        else:
            return instances.Get(token + '_' + instance.__name__)

    @staticmethod
    def InitializeGenericInstance(instances: PyDictionary, instance: T, parameters: List) -> T:

        if instances.Exist(instance.__name__) is False:
            genericInstance: T = instance(*parameters)
            instances.Add(instance.__name__, genericInstance)
            return genericInstance

        else:
            return instances.Get(instance.__name__)

