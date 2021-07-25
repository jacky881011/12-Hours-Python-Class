# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters: expression 

def double(x):
    return x*2

print(double(5))



double1 = lambda x : x*2
multiply = lambda x,y : y*x
add = lambda x,y,z: x+y+z
full_name = lambda first_name, last_name: first_name+" "+last_name

# also can use if statement
age_check = lambda age : print("Upper >18") if age >= 18 else print("Under <18")


print(double1(5))
print(multiply(4,3))
print(add(3,4,5))
print(full_name('Ming Yun','Hsu'))
age_check(20)
age_check(10)


function1 = lambda : print("Hello world")
function1()


add2= lambda x,y : print(x+y)
add2(9999999999,1)