class Animal:

    alive = True
    #def __init__(self,name,size):
     #   self.name = name
      #  self.size = size

    
    def Eat(self):
        print('This animal is eatting.')

    def Sleep(self):
        print('This animal is sleeping')


# Child
class Rabbit(Animal):                   # class Child( Parent )
    def Run(self):                      # Have there own method to execute
        print("This rabbit is runing")

# Child
class Fish(Animal):                   # class Child( Parent )
    def Swim(self):
        print("This fish is swimming")

# Child
class Hawk(Animal):                   # class Child( Parent )
    def Jump(self):
        print("This hawk is jumpping")


rabbit= Rabbit()
fish = Fish()
hawk = Hawk()

#rabbit.Sleep()
#fish.Sleep()
#hawk.Sleep()

rabbit.Run()
fish.Swim()
hawk.Jump()



