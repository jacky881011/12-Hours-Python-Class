# keywords arguments = arguments preceded by an identified when we pass them to a function
#                      The order of the arguments doesnt matter, unlike positional arguments
#                      Python knows the names of the arguments that our funciton receives


def hello(first, middle, last):
    print("Hello "+first+" "+ middle+" "+last)


# can change the order to use different location
hello(last= "Code",first= "Bro",middle= "Dude")