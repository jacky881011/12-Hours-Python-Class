import os                               # include to call the computer OS 


# test txt file
print("---------File Test---------")
path_file = "C:\\Users\\jacky hsu\\Desktop\\TestData.txt"               # need double \\ 

if(os.path.exists(path_file)):
    print("The location exits!")
    if os.path.isfile(path_file):
        print("That is a file.")
    
else:
    print("File is not exist.")


print()
print()
print("--------Folder Test----------")
# test the folder
path_file = "C:\\Users\\jacky hsu\\Desktop\\Test_folder"               # need double \\ 

if(os.path.exists(path_file)):
    print("The location exits!")

    # assess whether file or directory
    if os.path.isfile(path_file):                       
        print("That is a file.")

    elif os.path.isdir(path_file):
        print("That is a directory")
    
else:
    print("File is not exist.")
