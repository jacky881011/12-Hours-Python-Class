# Higher Order Function = a function that either:
#                         1. accepts a function as an argument
#                         2. returns a function
#                           (In python, functions are also treated as objects)


# test1
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):                    # outside function have higher order functions
    text = func("Hello")

    print(text)


hello(loud)
hello(quiet)


# test2
def dvisor(x):
    def dividend(y):
        div = y/x
        return div

    return dividend

divide = dvisor(2)
print(divide(10))           # 所以說 dividend有最高得優先權