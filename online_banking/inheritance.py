
class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping...............")

class Predator:
    def hunting(self):
        print(f"{self.name} is hunting")

class Prey:
    def flee(self):
        print(f"{self.name} is hunting by another")

class  Dog(Animal, Predator, Prey):

    def sound(self):
        print(f"{self.name} is barking UFF UFF")

class Cat(Animal):
    pass

dog1 = Dog("scooby")
dog1.sleep()
dog1.sound()
dog1.hunting()

cat1 = Cat("cheik")
cat1.eat()