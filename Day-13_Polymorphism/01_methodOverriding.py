#method overriding example:
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
class Cat(Animal):
    def sound(self):
        print("Meow")
for obj in [Dog(), Cat()]:
    obj.sound()   # different outputs