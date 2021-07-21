# **kwargs = parameter that will pack all arguments into a dictionary 
#            useful so that a function can accept a varying amount of keyword arguments



def hello(**tuple1):        # kwargs 可以自己變換名稱
    print(tuple1.get('first'))
    print(tuple1.values())
    print(tuple1.keys())

    for keys,values in tuple1.items():
        print(keys)
        print(values)



hello(title = "Jacky", first = "Bro", middle = "Dude", last = "Code")



