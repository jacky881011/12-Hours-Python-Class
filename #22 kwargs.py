# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amount of keyword arguments



def hello(**kwargs):        # kwargs 可以自己變換名稱

    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")



hello(title = "Jacky", first = "Bro", middle = "Dude", last = "Code")



