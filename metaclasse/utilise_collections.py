class MyDict(dict):
    def __setitem__(self, key, value):
        print(f"Setting {key} = {value}")
        super().__setitem__(key, value)

d = MyDict(a=1)
d['b'] = 2  # Appelle __setitem__ #Setting b = 2
print(d)
d.update({'c': 3})  # Ne passe pas par __setitem__ !

from collections import UserDict

class MyUserDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} = {value}")
        super().__setitem__(key, value)


d = MyUserDict(a=1)
d['b'] = 2  # Appelle __setitem__ #Setting b = 2
print(d)
d.update({'c': 3})  # passe par __setitem__ !