from car import Car
from car import Factory

car_1 = Car("Tesla",'Model Y',2021,'blue')
car_2 = Car("Tesla","MOdel X",2021,'White')

print(car_1.make)
print(car_1.color)
print(car_1.year)
print(car_1.model)

print(car_2.make)


car2 = Car('Tesla','Model 3',2022,'blue')
car2.Drive("$20000000")
car2.Stop()


car3 = Car('Tesla','Model 3',2022,'blue')
car3.Stop()


fac1 = Factory()
fac1.washed()
