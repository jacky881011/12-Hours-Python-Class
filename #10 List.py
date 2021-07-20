# list = used to store multple items in a single variable

food = ['pizza','hamburger','hot dog','spaghetti']

print(food)

# Show all items in lists
for items in food:
    print(items+" ",end="")


print()
food[3] = 'pudding'     # change the items
print(food)

# list function 

# remove
food.remove('hot dog')
print(food)

# pop
food.pop()              # remove the last one item in the list
print(food)

# append
food.append('ice cream')
print(food)

# insert
food.insert(0,'cake')
print(food)

# sort
food.sort()
print(food)

# clear
food.clear()
print(food)             # remove the all things from list