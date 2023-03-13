class Animal :      # Base class/Parent class

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def Display(self):
        print(self.breed, self.age)

Ani = Animal("Cat", 3)
print("Calling method of base class")
Ani.Display()

class Dog(Animal):        # Derived Class/ Inherited Class

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def print(self):
        print(self.breed, self.age)

Dogo = Dog("Bull Dog", 4)
print("Calling methods of both the classes")

Dogo.print()
Ani.Display()
