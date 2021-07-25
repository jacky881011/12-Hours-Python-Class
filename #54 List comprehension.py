# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [ expression for item in iterable]
#                      list = [ expression for item in iterable if conditional]
#                      list = [ expression if/else for item in iterable]

#ex
squares =[]                     # create an empty list
for i in range(1,11):             # create a for loop
    squares.append(i * i)       # define what each loop iteration should do
print(squares)


squares= [i*i for i in range(1,11)]
print(squares)


students = [100,90,80,70,50,40,30,20,10]
fail = list(filter(lambda data :data <60 , students))
print(fail)

failed_student = [i for i in students if i<60 ]
print(failed_student)

failed_student = [i if i>=60 else "Failed" for i in students]
print(failed_student)
