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