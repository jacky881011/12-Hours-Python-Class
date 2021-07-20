# str.format() =  optional method that gives users
#                 more control when displaying output
#                 like java %d %s

animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal,item))      #set the {} .format(first,second)
print("The {1} jumped over the {0}".format(animal,item))      #set the {} can set the order too
print("The {animal1} jumped over the {animal2}".format(animal1 = "cow1",animal2 = "cow2")) 
print("The {animal2} jumped over the {animal2}".format(animal1 = "cow1",animal2 = "cow2")) 


# 2
class_name = "science"
student  = "Jacky"

text = "{} is  in the {} class."
print(text.format(student,class_name))

# 3
name = "bro"
print("Hello my name is {:10}. Nice to meet you.".format(name))     # 空格10格
print("Hello my name is {:<10}. Nice to meet you.".format(name))     # 字體靠左
print("Hello my name is {:>10}. Nice to meet you.".format(name))     # 字體靠右
print("Hello my name is {:^10}. Nice to meet you.".format(name))     # 字體至於中間

# 4 numbers
number = 100
print("You are number {}".format(number))

pi = 3.1415926
print("The pi is {:.2f}".format(pi))            # 小數點第二位  two digits

money = 10000
print("Your money have {:,}".format(money))     # 就是在千位的地方標註

binary_change = 16
print("Binary 16 is {:b}".format(binary_change))        # 2進位
print("Binary 16 is {:o}".format(binary_change))        # 8進位
print("Binary 16 is {:X}".format(binary_change))        # 16進位
print("Binary 16 is {:E}".format(binary_change))        
