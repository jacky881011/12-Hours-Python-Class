# reduce( ) = apply a function to an iterable and reduce it to a single cumulative value         
#             performs function on first two elements and repeats process until 1  values remains
#
# reduce( function , iterable )

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce( lambda x,y : x + y, letters)   # 類似於不停往後加上新的字
print(word)

number = [5,4,3,2,1]
word = functools.reduce( lambda x,y : x * y, number)
print(word)

number = [1,1,2,3,5,8]
phas = functools.reduce( lambda x,y: x+y, number)
print(phas)