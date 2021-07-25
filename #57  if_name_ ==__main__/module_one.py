# 
# if __init__ == '__main__'

# y who?
# 1. module can  be run as a standalone program 
# 2. module can be imported and used by other module

# Python interpreter sets "special variables" , one of which is __name__
# then Python will execute the code found within __main__

# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run 

import module_two       # use the other module

def hello():
    print("Hello!")





if __name__ == '__main__':
    print('running this module directly')
else:
    print("ruinning other module indirectly. ")
