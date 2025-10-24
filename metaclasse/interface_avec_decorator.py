from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def jump(self):
        return f"{self.__class__.__name__} is jumping"

class Dog(Animal):
    def speak(self):
        print("OK")

dog = Dog()
