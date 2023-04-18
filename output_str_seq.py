import ast
AllSymbols = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

Enter = input("請輸入字串的陣列:") #輸入A~T不同順序的字串排列
#Enter = ['M','H','J','T','I','S','G','Q','F','P','E','O','D','N','B','L','A','K','C','R'] < 假設
EnterRng = ast.literal_eval(Enter) #將輸入的字串還原成它能夠轉化成的資料型別，此處轉為list

for eachEng in (EnterRng): 
    Seq = (AllSymbols.index(eachEng))+1 #陣列從1開始算，看該字母位於第幾個位置，該值就為seq
    AllSymbols.remove(eachEng) #剔除已找到seq的字母，繼續找下一個字母的位置

    print (Seq)

   