# Loop Control Statements = change a loops execution from its normal sequence

# break     =           used to terminate the loop entirely 
# continue  =           skips to the  next iteration of the loop 
# pass      =           does nothing, acts as a placeholder




# break method
name = ""
i= 0
while( len(name)==0):
    i=i+1
    print(str(i) +" ",end="")
    if(i==10):
        break

print(' End! ')


# continue method
phone_number = "123-456-789"

print("Your phone number is: ")
for i in phone_number:
    if(i=='-'):
        continue                # skips all '-', i dont want to show
    print(i,end="")             # end="" 指的就是要橫向顯示結果


print()
# pass method 
for i in range(1,21):
    if(i==13):                  # when i==13 then pass it 
        pass
    else:
        print(i)

print("End the program")




# Print the number of each student
number = '107360118'
for i in range(len(number)):
    if (i<=6):
        pass
    else:
        print(number[i],end="")
    
        