from meross.tools.dictionary import PyDictionary
from meross.abstractions.context.context_interface import IContext
from typing import TypeVar, List, Callable, Dict

T = TypeVar("T")


class SingletonHelper:

    @staticmethod
    def initializeContext(instances: PyDictionary, instance: Callable, *args) -> IContext:

        token: str = args[0] if args[0] is not None else None

        if token:
            instanceExist = instances.Exist(token)

        else:
            instanceExist = False

        if instanceExist is False:
            newInstance: IContext = instance(*args)
            dictionaryKey: str = newInstance.token
            dictionaryValue: Dict = {instance.__name__: newInstance}
            instances.Add(dictionaryKey, dictionaryValue)

            if instances.Exist(dictionaryKey):
                return newInstance

        else:
            userProfile = instances.Get(token)
            userContext = userProfile[instance.__name__]
            return userContext

    @staticmethod
    def initializeGenericInstance(instances: PyDictionary, instance: T, parameters: List) -> T:

        if instances.Exist(instance.__name__) is False:
            genericInstance: T = instance(*parameters)
            instances.Add(instance.__name__, genericInstance)
            return genericInstance

        else:
            return instances.Get(instance.__name__)
