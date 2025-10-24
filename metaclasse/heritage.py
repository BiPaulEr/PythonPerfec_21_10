
class A():
    def method(self):
        print("A")

    def methode_2(self):
        print("A2")

    def methode_3(self):
        print("A3")

class B(A):
    def methode_2(self):
        print("B2")
    
    def methode_3(self):
        print("B3")
        super().methode_3()

b =B()
b.method()
b.methode_2()
b.methode_3()

print(b.__hash__()) #154093395015