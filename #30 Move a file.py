import os
source = "#30folder"
destinaiton = "C:\\Users\\jacky hsu\\Desktop\\#30folder"


try:
    if os.path.exists(destinaiton):
        print('There is already a file there')
    else:
        os.replace(source,destinaiton)
        print('Already move the file: '+source)


except FileNotFoundError:
    print(source+'  was not found')

