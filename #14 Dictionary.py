# dictionary = A changeable, unordered collection of unique key : value pairs
#              fast because they use hashing, allow us to access a value quickly


dict1 = {'USA': 'Wahington DC',
        'India': 'New Dehli',
        'China': 'Bejing',
        'Russia': 'Moscow'}

#print(dict1['India'])\


# get method
print(dict1.get('Russia'))      # show the keys value we want

# key method
print(dict1.keys())             # show all keys from dicitonary

# values method
print(dict1.values())           # show all key's values

# items method 
print(dict1.items())            # show the items inside the dictionarys



# show the all things
for key,value in dict1.items():
    print(key)
    print(value)


# update method (add mew items from dictionary)
dict1.update({'Germany': 'Berlin'})
print(dict1.items())

# update method (change the key's value from old)
dict1.update({'USA': 'Las Vegas'})
print(dict1.items())

# pop method (remove the keys(also values) we dont want)
dict1.pop('China')
print(dict1.items())

# clear method (remove all the items on the dictionary)
dict1.clear()
print(dict1.items())

