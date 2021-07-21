# tuple = collection which is ordered and unchangeable
#         used to group together related data
# ( ): tuple

student = ('Bro', 21, 'male','Bro')

print(student)

print(student.count('Bro'))     # show the count on 'Bro' times 

print(student.index('male'))    # show the index on male


for x in student:
    print(x)

if 'Bro' in student:            
    print("Bro is here!")

# student.append('kkk')     tuple cant change to do anything 


