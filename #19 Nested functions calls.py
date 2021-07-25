# nested functions calls = function calls inside other fumction calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function 

import math



# ex
num = 3.14
num = float(num)
num = abs(num)
num = round(num)
print(num)





# test nested function :find sqrt value
def print_value(value):
    ans = dividend(value)                   # nested function 
    print("The math.sqrt is: "+str(ans))
    


def dividend(number):
    number = math.sqrt(number)
    return number

print_value(64)
print_value(33)



menu = []
def add_menu(food):
    new_menu  = add_food(food)
    show_menu(new_menu)



def add_food(food):
    menu.append(food)
    return menu

def show_menu(update_menu):
    print("This is the new menus item!")
    for items in update_menu:
         print(items)


new_foods = ['cola','ice cream','juice','wine']
add_menu(new_foods)
print(len(menu))
new_foods2 = ['cola','ice cream','juice','wine']
add_menu(new_foods2)

