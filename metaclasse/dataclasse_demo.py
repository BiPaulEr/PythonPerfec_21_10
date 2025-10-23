class Vector(object):
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"<Vector: x={self.x}, y={self.y}, z={self.z}>"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 3)
v3 = Vector(1, 2, 3)

print(v1) #<Vector: x=1, y=2>

print(v1 == v3)

from dataclasses import dataclass

@dataclass(order=True)
class Vector3d:
    x : int 
    y : int = 2
    z : int = 0


v1 = Vector3d(1, 2, 3)
v2 = Vector3d(2, 3)
v3 = Vector3d(1, 2, 3)

print(v1) #<Vector: x=1, y=2>

print(v1 == v3)
print(v1 > v2)