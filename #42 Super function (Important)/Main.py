# super() = Function used to give acess to the methods of a parent class 
#           Returns a temporary object of a parent class when used

#-------------------------------no use super-------------------------------------------
class Rectangle:
    pass

class Square(Rectangle):

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


square = Square(3,3)
cube = Cube(3,3,3)

#-------------------------------use super-------------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)         # use the variable from the Parent(Rectangle)
    
    def area(self):
        return self.length * self.width
    
    


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height                # different from parent class variable 

    def area(self):
        return self.length * self.width * self.height


square = Square(3,3)
area_square = square.area()
print("The square area is: "+str(area_square))
cube = Cube(3,3,3)
area_cube = cube.area()
print("The cube area is: "+str(area_cube))









#----------------------------------------------------------test------------------------------------------------------------------
class Rectangle2(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def find_area(self):
        return self.length * self.width

class Rectangle3(Rectangle2):
    def __init__(self, length, width ,height):
        super().__init__(length, width)
        self.height = height
    
    def find_area(self):
        return self.length * self.width * self.height


rec = Rectangle2(4, 5  )
rec2 = Rectangle3(4 ,5 ,6)

area2 = rec2.find_area()
area = rec.find_area()

print(area2)
print(area)