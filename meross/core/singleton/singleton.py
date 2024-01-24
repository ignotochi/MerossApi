from typing import TypeVar, Callable
from meross.abstractions.context.context_interface import IContext
from meross.core.exeptions.exceptionManager import ExceptionManager
from meross.core.logger import MerossLogger
from meross.core.singleton.SingletonHelper.singletonHelper import SingletonHelper
from meross.tools.dictionary import PyDictionary

T = TypeVar("T")


class Singleton:
    instances: PyDictionary = PyDictionary()

    @classmethod
    def New(cls, instance: T) -> T:

        def Create(*args) -> T:

            if issubclass(instance, IContext):
                contextInstance: Callable = instance
                context = SingletonHelper.initializeContext(cls.instances, contextInstance, *args)
                return context

            else:
                genericInstance: Callable = instance
                newGenericSingletonInstance = SingletonHelper.initializeGenericInstance(cls.instances, genericInstance, *args)
                return newGenericSingletonInstance

        return Create

    @classmethod
    def get(cls, key):
        instance = cls.instances.Get(key)

        if instance is not None:
            return instance
        else:
            return None

    @classmethod
    def clean(cls, key):
        try:
            instance = cls.instances.Get(key)

            if instance is not None:
                cls.instances.Delete(key)

        except Exception as exception:
            MerossLogger("Singleton.clean").writeErrorLog(ExceptionManager.catch(exception))
            raise Exception("Context cleaning failde")

