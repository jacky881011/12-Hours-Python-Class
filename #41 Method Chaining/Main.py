# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self


class Car:
    def turn_on(self):
        print("You start the engine")
        return self 
    
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You break the car")
        return self
    
    def turn_off(self):
        print("You turn off the engine")
        return self



car1 = Car()
#car1.turn_on()   # not add return self 
#car1.drive()     # not add retrun self 


# 可以不斷地進行疊加處理方法 multiple methods sequentially
car1.turn_on().drive()
car1.turn_on().drive().brake().turn_off()
