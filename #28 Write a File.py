
text1 = "\n(Append) Have a nice day! See ya"
text2 = "Hello Bro!\nWelcome to Python Class\nAmazing for 12 Hours!\n"

with open('C:\\Users\\jacky hsu\\Desktop\\Read_text.txt','w') as file1:     # Rewrite the text  in the text file (覆寫 會遮蓋先前的資料)
    file1.write(text2)

with open('C:\\Users\\jacky hsu\\Desktop\\Read_text.txt','a') as file1:     # Append the text in the text file (延伸繼續寫新的資料)
    file1.write(text1)








#Read

try:
    with open('C:\\Users\\jacky hsu\\Desktop\\Read_text.txt') as file1:
        print(file1.read())
    file1.close()

except FileNotFoundError:                               # if not found the file 
    print("That file was not found :( ")