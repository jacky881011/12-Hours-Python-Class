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

students = sorted(students)                             # sorted(students,reverse= True) 顛倒顯示

for i in students:
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
sorted_students = sorted(students,key = score)

for i in sorted_students:
    print(i)



dic1 = [('Jacky','107360118','A'),
        ('Melody','107381023','A'),
        ('Kevein','107360129','F'),
        ('Patrick','107371022','B'),
        ('Lisa','107367821','D'),
        ('Lpoee','107389011','C')]

sub_dic1 = lambda dic1 : dic1[2]
dic1.sort(key= sub_dic1)

for i in dic1:
    print(i)


