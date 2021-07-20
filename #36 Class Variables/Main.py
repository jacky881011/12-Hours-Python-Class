from car import Car


car_1 = Car('Tesla','Model Y',2022,'White')
car_2 = Car('Tesla','Model 3',2021,'Blue')


# class method 
car_1.Driving()
car_1.Stopping()

car_2.Driving()
car_2.Stopping()



car_1.wheels = 2        # only car_1 wheels be the 2

print(car_1.wheels)
print(car_2.wheels)


Car.wheels = 6          # change the variables form the class, and all object use is the same
print(Car.wheels)
print(car_2.wheels)

