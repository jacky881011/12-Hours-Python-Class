
# thread = a flow of execution. Like a seperate order of instructions.
#          However each thread takes a turn running to achieve concurrency 
#          GIL = (global interpreter lock),
#          allows only one thread to hold the control or the Python interpreter at any one time

#   cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#               use multiprocessing 

#   io bound = progrma/task spends most of it's time waiting for external events (user input , web scraping)
#               use mutithreading

import threading
import time


print(threading.enumerate())        # [<_MainThread(MainThread, started 14496)>]

# three task 

def eat_breakfast():
    time.sleep(2)
    print("You eat breakfast")



def drink_coffee():
    time.sleep(7)
    print("You drank coffee")



def study():
    time.sleep(3)
    print("You finished study")


# sequential function (not threading)
#eat_breakfast()
#drink_coffee()
#study()

# set the thread order
x=  threading.Thread(target = eat_breakfast , args = ())
x.start()

y=  threading.Thread(target = drink_coffee , args = ())
y.start()

z=  threading.Thread(target = study , args = ())
z.start()


# 讓所有function同時進行
x.join()
y.join()
z.join()




print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())