# set = collection which is unordered, unindexed. No duplicate value(不會有重複的項目 所以可以自動消除重複的元素)
# { }: sets
#只有set的形式可以去做交集、聯集以及差集  list tuple皆無法去做這項功能

utensils = {'fork','spoon','knife','fork'}
dishes = {'bowl','plate','cup'}
print(utensils)


utensils.add("nepkin")
print(utensils)

utensils.remove('fork')
print(utensils)

# update dishes in utensils
utensils.update(dishes)

for items in utensils:
    print(items)



# Just set() can use union、intersection、difference

utensils2= {'fork','spoon','knife','fork'}
dishes2 = {'bowl','plate','cup'}

# union  聯集
print()
print("Union")
dinner_table = utensils2.union(dishes2)

for items in dinner_table:
    print(items)


# intersection  交集
print()
print("Intersection:")
dinner_table = utensils2.intersection(dishes2)


if(len(dinner_table) == 0 ):            # if two element not intersection with each other
    print('Nothing inrersection')
else:
    for x in dinner_table:
        print(x)

# difference    差值
print()
print("Difference:")
dinner_table = utensils2.difference(dishes2)
for items in dinner_table:
    print(items)






