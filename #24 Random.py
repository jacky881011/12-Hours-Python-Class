import random

#1
roll = random.randint(1,6)              # random number of integer (first,end)
roll2 = random.random()                 # random number conclude float and integer
print(roll)
print(roll2)



#2
game = ['rock','pepper','scissors']
ans = random.choice(game)               # random to get the item from the list

# or under method
order = random.randint(0,len(game)-1)
print(game[order])


# 3
cards = [2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)                   # to distroy the order of list 

print(cards)


