# return statement = Functions send Python values/ objects back to the caller.
#                    These values/ objects are known as the funciton's returns value


from typing import Sized


def add(number1,number2):
    number = number1 + number2
    
    return number

print()
print("========Add========")
sum = add(17,18)
print(sum)


def multi(number1,number2):
    return number1 * number2

print()
print("========Multiple========")
mul = multi(17,5)
print(mul)



