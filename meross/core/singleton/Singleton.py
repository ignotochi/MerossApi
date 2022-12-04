from typing import TypeVar, Callable
from meross.abstractions.context.IContext import IContext
from meross.core.singleton.SingletonHelper.SingletonHelper import SingletonHelper
from meross.tools.PyDictionary import PyDictionary

T = TypeVar("T")


class Singleton:
    instances: PyDictionary = PyDictionary()

    @classmethod
    def New(cls, instance: T) -> T:

        def Create(*args) -> T:

            if issubclass(instance, IContext):
                contextInstance: Callable = instance
                context = SingletonHelper.InitializeContext(cls.instances, contextInstance, *args)
                return context

            else:
                genericInstance: Callable = instance
                newGenericSingletonInstance = SingletonHelper.InitializeGenericInstance(cls.instances, genericInstance, *args)
                return newGenericSingletonInstance

        return Create

    @classmethod
    def Clean(cls, key):
        instance = cls.instances.Get(key)

        if instance:
            cls.instances.Delete(key)
