from selenium import webdriver
import time
import requests
import json

# User Login
ul_headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'eeeyyyyhhhh'} #表頭
ul_data = {'account': 'juliachan0307', 'password': 'juliachan0307'} #Body
r1 = requests.post('http://test/user/login', headers= ul_headers, data= ul_data) 
j = json.loads(r1.text) #將json解碼成python對象
user_token = j['usertoken'] #取得usertoken

# Game Login    
gl_headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'aaabbbccc'}
with open('code.txt','r') as f: #輸入要截圖哪幾款
    data = f.read()
    t_list = data.split()

input_num = input('輸入階層: ') #總共有幾個階層

for i in t_list: #依序取得欲截圖的款式連結
    i = str(i)
    gl_data = {'usertoken': user_token, 'lang': 'zh-cn'}
    r2 = requests.post('http://test/user/gamelink', headers= gl_headers, data= gl_data)
    j = json.loads(r2.text)
    link = j['url'] #取得該款式連結

    browser = webdriver.Chrome() #啟動webdriver開啟網頁
    browser.get(link)
    time.sleep(5)

    for j in range(1,input_num+1): #決定幾個階層就截圖幾張
        if j == 1:
            browser.save_screenshot( i + '-1.png')
        else:
            browser.execute_script('PIXI.game.world.children[0].btnctrl.callBtnEvent("Btn_Add")')
            browser.save_screenshot(i+ '-' + str(j) + '.png')
    browser.close()
