# *args = parameter that will pack all arguments into a tuple=()
#         useful so that a function can accept a varying amount of arguments

def add(number1,number2):
    sum = number1 + number2
    return sum


print(add(1,333))




def add(*args):                 # can change -args- name to any kinds of. like stuff ...etc
    sum = 0
    args = list(args)           # args is a tuple() can't changeable so need to change list, in order to change inside elements
    args[0] = 0

    for i in args:
        sum += i
    
    return sum

print(add(1,2,3,4,5,6))




def combine_string(*char):
    string = ""
    char = list(char)                   # change to list become changeable

    char[len(char)-1] = " Melody"
    for x in char:
        string = string + x

    return string



print(combine_string("Hi"," my"," name"," is"," Jacky!"))

