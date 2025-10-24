class InterfaceValidator(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        #print(mcs, "__new__ called")
        cls = super().__new__(mcs, name, bases, namespace)
        if "execute" not in namespace or not callable(namespace["execute"]):
            raise Exception(f"execute not implemented in {cls}")
        print(namespace)
        return cls

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        #print(mcs, "__prepare__ called")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        
        #print(cls, "__init__ called")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        #print(cls, "__call__ called")
        return super().__call__(*args, **kwargs)

print("AVANT LA CREATION DE RevealingClass")

class Class1(metaclass=InterfaceValidator):
    attribut =3
    def execute(self):
        print("execute")

class Class2(metaclass=InterfaceValidator):
    execute = 4
    pass 

class1 = Class1()
class2 = Class2()