# 2D-List = a list of lists

menu_list =[['coffee','cola','lemon juice'],['pizza','hamburger','hot dog'],['cake','ice cream']]
print(menu_list)


print(menu_list[0])
print(menu_list[1])
print(menu_list[2])


#print(menu_list[0][2])
#print(menu_list[1][2])
#print(menu_list[2][1])

for items in menu_list:
    print(items[1])



print()
i=0
print("-----------------------------------Test-------------------------------------------")
for items_1d in menu_list:
    i+=1
    for items_2d in items_1d:
        print(items_2d,end = " ")
        print("From "+str(i)+ " row of list")