class Animal:
    def Eat(self):
        print("The animal is eating")



class Rabbit(Animal):
    # Override  就是直接宣告一個相同的方法即可
    def Eat(self):
        print("This rabbit is eatting a carrot")


rabbit = Rabbit()       # the object from Rabbit
rabbit.Eat()
