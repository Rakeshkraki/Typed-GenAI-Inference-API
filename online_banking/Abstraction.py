
from abc import ABC , abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print(f"car is starting")

    def stop(self):
        #print(f"car is stopped")
        pass
        
supra = Car()
#supra.start()
