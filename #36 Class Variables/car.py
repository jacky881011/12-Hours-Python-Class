
class Car:
    wheels = 4  # class variable

    def __init__(self,make,model,year,color):
        self.make = make        # instance variable
        self.model = model      # instance variable
        self.year = year        # instance variable 
        self.color = color      # instance variable

    def Driving(self):
        print("The car "+self.model+" is driving")
        
        


    def Stopping(self):
        print("The car "+self.model+" is stopping.")
       

