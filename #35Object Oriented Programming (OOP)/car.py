class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def Drive(self,price):
        self.price = price
        print('Car is driving')
        print('The Car '+self.model+' is driving!')
        print("Its price is "+ price)
    
    def Stop(self):
        print('Car is stopping')


class Factory:

    def fixed(self):
        print("The car is fixed!")

    def washed(self):
        print("The car is washed!")