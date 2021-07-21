import random
import time

#1
roll = random.randint(1,6)              # random number of integer (first,end)
roll2 = random.random()                 # random number conclude float and integer
print(roll)
print(roll2)

for i in range(10):
    ra = random.randint(0,10)
    print(ra)
    time.sleep(0.8)





#2
game = ['rock','pepper','scissors']
ans = random.choice(game)               # random to get the item from the list
print("ans(Random): "+ ans)

# or under method
order = random.randint(0,len(game)-1)
print(game[order])


# 3
cards = [2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)                   # to distroy the order of list 

print(cards)

