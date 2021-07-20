# logocal operators (and, or, not)=  used to check if two or more conditional statement 
# Use (and, or, not), not && ||

#temp = int(input("What is the temperature outside?: "))
temp = 30

if (temp>=18 and temp<30):
    print("The temperature is great today")

elif (temp>=30 or temp<18):
    print("The temperature is bad today")



# not()  false to true, true to false
check = True
print(not(check))


if not(temp>=18 and temp<30):
    print("The temperature is bad today")

elif not(temp>=30 or temp<18):
    print("The temperature is great today")
   
    


        