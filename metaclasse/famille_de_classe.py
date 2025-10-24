class PluginsBase(type):
    list_des_classes = {}
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, "__new__ called")
        cls = super().__new__(mcs, name, bases, namespace)
        mcs.list_des_classes[name] = cls
        return cls

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "__prepare__ called")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        
        print(cls, "__init__ called")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, "__call__ called")
        return super().__call__(*args, **kwargs)

print("AVANT LA CREATION DE RevealingClass")

class Class1(metaclass=PluginsBase):
    pass
class Class2(metaclass=PluginsBase):
    pass

class1 = Class1()
class2 = Class2()

print(PluginsBase.list_des_classes) #{'Class1': <class '__main__.Class1'>, 'Class2': <class '__main__.Class2'>}
