# sort() method = used with lists  [ ]   no tuple or dictionary
# sorted() function = used with iterables



#----------------------------------------------list use sort function------------------------------------------------------
students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]       #list 
number = [1,3,4,2,6,5,8,9,10]

students.sort()

for i in students:
    print(i)

print()
print()
students.sort(reverse = True)

for i in students:
    print(i)

#----------------------------------------------tuple use sorted------------------------------------------------------
print()
print()
students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")           # tuple (cant use sort function )

sorted_student = sorted(students)                             # sorted(students,reverse= True) 顛倒顯示

for i in sorted_student:
    print(i)


#----------------------------------------------advance list conclude tuple------------------------------------------------------
print()
print()
students = [('Jacky','F',60),
            ('Melody','A',90),
            ('Patrick','B',80),
            ('Mr .Krabs','C',78),
            ('Kevin','D',70)]

grade = lambda grades : grades[2]                   # chose the column you want to sort (Any)
students.sort(key = grade ,reverse = True)          # need A,B,C


for i in students:
    print(i)

#----------------------------------------------advance tuple conclude tuple (cant use sort)------------------------------------------------------
print()
print()
students = (('Jacky','F',60),
            ('Melody','A',90),
            ('Patrick','B',80),
            ('Mr .Krabs','C',78),
            ('Kevin','D',70))

score = lambda scores : scores[1]
sorted_students = sorted(students,key = score, reverse= True)

for i in sorted_students:
    print(i)