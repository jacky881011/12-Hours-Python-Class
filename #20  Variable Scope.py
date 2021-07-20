# scope = The variable is recognize
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created


name = "Hi global scope" # global scope (available inside and outside function)


def display_name():
    name = "local scope"           # local scope (available inside this function)
    print("Hi "+name)


print(name)
display_name()

