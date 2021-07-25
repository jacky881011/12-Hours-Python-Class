# muti-level inheritance = when a derived (child) class inherits another derived (child) class 
# 
# 
class Organism:
    alive = True

    def Show(self):
        print("All the animals are animals.")



class Animal(Organism):
    def Eating(self):
        print("This animal is eating")


class Dog(Animal):
    def Bark(self):
        print("This dog is bark!")



dog = Dog()          # object from the Dog class
dog.Show()
dog.Bark()
dog.Eating()        # from animals