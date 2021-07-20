# multiple inheritance = when a child class is derived from more than one parent class

from typing_extensions import ParamSpec


class Prey:
    def Flee(self):
        print('This animal flees')



class Predator:
    def Hunt(self):
        print('This animal is hunting')



class Fish(Prey,Predator):      # The child class can derived more than one class
    pass

class Hawk(Prey,Predator):
    pass

class Rabbit(Prey,Predator):
    pass


# The object from the class
fish = Fish()
hawk = Hawk()
rabbit = Rabbit()



rabbit.Flee()
hawk.Flee()
fish.Flee()

rabbit.Hunt()
fish.Hunt()
hawk.Hunt()
