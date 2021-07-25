# zip (*iterables) = aggreate elements from two or more iterables (list , tuples , sets, etc...)
#                    creates a zip object with paired elements stored in tuples for each element

username = ["dude", "Bro","Mister"]
passwords = ("p@ssword", "anc123", "guest" ) 

users = zip( username , passwords)
print()
print(type(users))

for i in users:
    print(i)


users = list(zip( username , passwords))        # change to list
print()
print(type(users))
for i in users:
    print(i)



users = dict(zip( username , passwords))        #change to dictionary 
print()
print(type(users))

for key,value in users.items():
    print(value)
    print(key)


# more variables
username = ["dude", "Bro","Mister"]
passwords = ("p@ssword", "anc123", "guest" ) 
login = ["1/1/2021", "1/2/2021", "1/3/2021"]

user_data = list(zip(username, passwords , login))              # if three variables cant change to dictionary
for i in user_data:
    print(i)