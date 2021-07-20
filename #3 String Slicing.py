# slicing = create a substring by extracting elements from another string 
#           indexing[] or slice()
#           [start: stop : step]

name = "Ming Yun Hsu"

first_name = name[0:4:1]        #show the Ming  0~4
print(first_name)

last_name = name[9:]            # show the last name
print(last_name)

# step
step_name = name[0: 8: 2]
print(step_name)

# reverse
reverse_name =name[::-1]
print(reverse_name)



# String Slicing
website1= "https://google.com"
website2 = "http://wikipedia.com"

slice1 = slice(8,-4)        #slice(Start char, End char)
slice2 = slice(7,-4)

print(website1[slice1])
print(website2[slice2])


con = 'Happy Birthday!'
slice12 = slice(6,-1)
print(con[slice12])


