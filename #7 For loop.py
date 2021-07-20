#for loop = a statement that will execute it's block of code 
#           a limited amount of times
#           
#           while loop = unlimited 
#           for loop = limited


import time     # for thread to sleep
list1= ['Happy','sad','shock']

for i in range(10):
    print(i+1)


for i in range(50,100+1,2):
    print(i)

# print the elemets in the list
for i in list1:
    print(i)


for i in range(10,0,-1):
    print(i)
    time.sleep(1)       # sleep 1 seconds

print("Happy new year!")


