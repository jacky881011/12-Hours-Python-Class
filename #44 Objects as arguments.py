class Car:

    color = None

class Motorcycle(Car):
    pass


def change_color(vehicle,color):            # use method contain object, and change object   (object, )
    vehicle.color = color
    

car1 = Car()
car2 = Car()
car3 = Car()

motor1 = Motorcycle()
motor2 = Motorcycle()



change_color(car1,'blue')
change_color(car2,'red')
change_color(car3,'white')

change_color(motor1,'green')
change_color(motor2,'yellow')


print(car1.color)
print(car2.color)
print(car3.color)
print(motor1.color)
print(car3.color)
