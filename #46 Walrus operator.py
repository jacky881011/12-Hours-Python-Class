# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression 

# happy = True 
# print(happy)

print(happy := True)            # Use := (also print True)


#-----------------------Not Use Walrus-------------------------------------
foods = list()

while True:
    food = input('What food do you like?: ')
    if(food == "quit"):
        break
    foods.append(food)

print(foods)


#-------------------------Use Walrus----------------------------------------
foods = list()

while food := input("What food do you like?:") != "quit":               # means when user not input quit, always True
    foods.append(food)

print(foods)