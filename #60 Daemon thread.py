# daemon thread = a thread that runs in the background , not important for program to run 
#                 your program will not wait for daemon threads to complete before exiting 
#                 non-daemon threads cannot normally be killed, stay alive until task is complete 
#                 
#                 ex . background tasks, garbage collection, waiting for input , long running processes
#                      

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count +=1
        print("logged for "+ str(count) + " seconds")
        if count == 10:
            break
    end= "The Program is stop background"
    return end
    

x = threading.Thread(target=timer , daemon= True)   # 背景運作 
print(x.isDaemon())                             # check the daemon thread, 
x.start()



ans = input("Happy Time : ")


