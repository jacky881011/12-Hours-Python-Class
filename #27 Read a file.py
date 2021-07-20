# Read a file need to use "with open(file_path_fileName) as file(Name can change)""


with open('C:\\Users\\jacky hsu\\Desktop\\Read_text.txt') as file1:
    print(file1.read())


print(file1.closed)     #true 


print()
print()
print("The test is {}".format("Try except test"))

# because used to open file is a dangerous things must use (try except)
try:
    with open('C:\\Users\\jacky hsu\\Desktop\\Read_text.txt') as file1:
        print(file1.read())
    file1.close()

except FileNotFoundError:                               # if not found the file 
    print("That file was not found :( ")

