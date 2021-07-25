import os
import shutil

path = 'C:\\Users\\jacky hsu\\Desktop\\secret_message.txt'
path2 = '#30folder'
path3 = 'C:\\Users\\jacky hsu\\Desktop\\Test_folder'

#os.remove('#30Testfile.txt')

try:
    #os.remove(path)                         # delete a file                         將檔案刪除
    os.rmdir(path3)                        # delete an empty directory           刪除空資料夾
    #shutil.rmtree(path3)                   # delete a directory containing files  將整個資料夾包含檔案都刪除

except FileNotFoundError:
    print("That file was not found")            #already delete the file 
except PermissionError:
    print("You dont have the oermission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path3+' was deleted')



