# nested loop = The 'inner loop' will finish all of it's iterations before 
#               fifishing one iteration of the "outer loop"

rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        print('$', end ="")     # 平遞增顯示 
    print()                     # 結束一整列後換行

