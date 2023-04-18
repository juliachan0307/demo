import xlrd
import random

r_book = xlrd.open_workbook("abc.xlsx")
r_sheet = r_book.sheets()[0]
strip_num = 4 #串列的數量 

#先產出共有4個滾輪欄位的變數
col_lists = []
for i in range (1, strip_num+1):
    col = "col_list" + str(i)
    col_lists.append(col)

# col_list從文件中取得倍數
for i in range(len(col_lists)):
    col_lists[i] = [x for x in r_sheet.col_values(i+3) if x]  # R1的倍數欄全列出
    if i == 0:
        continue
    elif i == 3:
        for n in range (i+1):
            col_lists[i].append(0) 
        print (col_lists[i])
    else:
        for n in range (i):
            col_lists[i].append(0) 
        print (col_lists[i])

minA = float(input("最小值: ")) # 輸入最大/最小值範圍
maxB = float(input("最大值: "))

for i in range (10): 
    while True:
        #分別對col_list中的數字串隨機取第幾個值
        r1= random.randint(1,100) # 從1開始取，0為標題
        r2= random.randint(1,101)
        r3= random.randint(1,102)
        r4= random.randint(1,103)
       
        #把取到的第1~4的col_list中的數字串相加，看是否符合要查找的數字
        sum1= col_lists[0][r1]+col_lists[1][r2]+col_lists[2][r3]+col_lists[3][r4]
        sum2= round(sum1,2) # 取小數點後兩位

        if minA < sum2 <= maxB:
            R1= str(r1)
            R2= str(r2)
            R3= str(r3)
            R4= str(r4)
            break
    print(R1+','+R2+','+R3+','+R4 )  



