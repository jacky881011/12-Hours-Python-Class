# Prevents a user from creating an object of the class 
# + compels a user to override abstract methods in a child class 

# abstract class = a class which contains one or more abstrawct methods
# astract method = a method that has a declaration but does not have an implementation.

#-------------------------------not abstract-----------------------------------
class Vehicle:
    def go(self):
        pass


class Car(Vehicle):

    def go(self):
        print("The car is moving")

class Motor(Vehicle):

    def go(self):
        print("The motor is riding")

vehicle1 = Vehicle()

car1 = Car()
car1.go()

motor1 = Motor()
motor1.go()

#-------------------------------with abstract-----------------------------------
from abc import ABC , abstractmethod

class Vehicle2(ABC):                # 要使用抽象方法需要先繼承ABC 才可以宣告此為抽象的class
    @abstractmethod                 # 被繼承得class中的物件不能夠宣告與使用抽象class的方法 method
    def go(self):
        pass

    @abstractmethod
    def Stop(self):
        pass

class Car2(Vehicle2):

    def go(self):                   # Override the method
        print("The car is moving")

    def Stop(self):
        print("The car is stopped")

class Motor2(Vehicle2):

    def go(self):
        print("The motor is riding")

    def Stop(self):
        print("The motor is stopped")


car2 = Car2()
motor2 = Motor2()

car2.go()
motor2.go()

