# map() = applies a function to each item in an iterable (list, tuple, etc)
#
# map( function , iterable)


# store[( item_name , price , expendture )]
store = [('shirt',  20.00, 19),
         ('pants',  25.00, 20),
         ('jacket', 50.00, 12),
         ('socks',  10.00, 30)]


#def to_euros(data):
#    return data[0],data[1]*0.82

to_euros = lambda data: (data[0],data[1]*0.82, data[1]*0.82*data[2])
to_dollars = lambda data: (data[0],data[1]/0.82, data[2]*data[1]/0.82)


store_euros = list(map(to_euros,store))
store_dollars = list(map(to_dollars,store))

print(len(store))

print()
print()
for i in store_euros:
    print(i)

print()
print()
for i in store_dollars:
    print(i)



grocery = [('Class A', 10 , 150),
           ('Class B', 14 , 200),
           ('class C', 30 , 400)]

price = lambda grocery : (grocery[0], grocery[1]*grocery[2])

grocery = list(map(price , grocery))

for i in grocery:
    print(i)


cars_shop = [('Model 3',150, 20),
             ('Model S',300, 12),
             ('Model Y',200, 10),
             ('Model X',400, 10)]

for i in cars_shop:
    print(i)

shops = lambda data : (data[0], data[1] * data[2])

cars_shop = list(map(shops , cars_shop ))

for i in cars_shop:
    print(i)


print("Sorted")
sort_year = lambda data :data[1]

cars_shop = sorted(cars_shop, key = sort_year)

for i in cars_shop:
    print(i)
