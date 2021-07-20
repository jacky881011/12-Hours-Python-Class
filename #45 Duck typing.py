# duck typing = concept where the class of an object is less important than the methods / attributes
#               class type is not checked if minimum methods / attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("The duck is walking")
    
    def talk(self):
        print("The duck is qwuacking")


class Chicken:
    def walk(self):
        print("The chicken is walking")
    
    def talk(self):
        print("The chicken is clucking")

    
class Person():

    def catch(self,animal):
        animal.walk()
        animal.talk()
        print("Ypu get a duck")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)
    
