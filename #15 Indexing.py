# index operator [] = gives access to a sequence's element (str, list, tuples)
# 就是說可以去找出一個String 或 list 中的字。

name = 'bro Code'

if(name[0].islower()== True):
    name = name.capitalize()        # capitalize() means the first char of string be UperCase

print(name)         # Bro code


# test2
first_name = name[:3].upper()
print(first_name)

last_name = name[-4:].upper()
print(last_name)

last_charater = name[-1]
print(last_charater)

