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

    
class Person:

    def catch(self,animal,name):
        animal.walk()
        animal.talk()
        print("You get a "+ name)
        


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck,'duck')
person.catch(chicken,'chicken')
    

sum = 0
a = [1,1]
b=[]

for i in range(10):
    sum = a[i]+a[i+1]
    a.append(sum)

print(a)
