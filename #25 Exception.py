# exception = events detected during execution that interrupt the flow of a program 
# except + Exception name 

try:
    numerator = int(input("Enter a number ti divide: "))
    dividend = int(input("Enter a number to divide by: "))
    print("ans: "+str(numerator/dividend))
except ZeroDivisionError:                               # divide zero will show
    print("You cant divide by zero idiot!")
except ValueError:                                      # if input string then wrong
    print("Enter only number please")
except Exception:                                       # all the exception will print
    print("something went wrong : (")




try:
    numerator = int(input("Enter a number ti divide: "))
    dividend = int(input("Enter a number to divide by: "))
    result = numerator/dividend
except ZeroDivisionError as e:     
    print(e)                                            # divide zero willl show
    print("You cant divide by zero idiot!")
except ValueError as e:                   
    print(e)                                            # if input string then wrong
    print("Enter only number please")
except Exception as e:               
    print(e)                                            # all the exception will print
    print("something went wrong : (")
else:
    print(result)

finally:                                                # always do no matter what the result it 
    print("This will always execute!")





