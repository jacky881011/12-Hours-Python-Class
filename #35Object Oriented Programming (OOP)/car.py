class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def Drive(self):
        print('Car is driving')
        print('The Car '+self.model+' is driving!')
    
    def Stop(self):
        print('Car is stopping')