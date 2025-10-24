class RevealingMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, "__new__ called")
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "__prepare__ called")
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        cls.nombre_dinstance = 0
        print(cls, "__init__ called")
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        cls.nombre_dinstance +=1
        print(cls, "__call__ called")
        return super().__call__(*args, **kwargs)

print("AVANT LA CREATION DE RevealingClass")

class RevealingClass(metaclass=RevealingMeta):
    def __new__(cls):
        print("__new__", cls)
        self = super().__new__(cls)
        return self

    def __init__(self):
        self.attribut = "HELLO"
        print("__init__", self) #__init__ <__main__.RevealingClass object at 0x00000243423D9EE0>
        super().__init__()

    def method(self):
        print("methode", self.attribut)

reveal = RevealingClass()
reveal2 = RevealingClass()
print(reveal.nombre_dinstance)
print(RevealingClass.nombre_dinstance)