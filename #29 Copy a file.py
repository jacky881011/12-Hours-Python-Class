# copyfile() = copies contents of a file
# copy() = copyfile() +permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modificaiton times)


import shutil
import os
#shutil.copyfile('#29Testfile.txt','copy.txt')           #src,dst        (source , destination)
# copy the file(source) to the destination and have a name
shutil.copyfile('#29Testfile.txt','C:\\Users\\jacky hsu\\Desktop\\#29CopyFile.txt')


# Read the file
with open('C:\\Users\\jacky hsu\\Desktop\\#29CopyFile.txt') as file1:
    print(file1.read())

file1.close()

