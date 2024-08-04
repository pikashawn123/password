password = 'a123'
remain_time = 3
while remain_time >= 1:
    pwd = input('請輸入密碼: ')
    if pwd == password:
            print('輸入成功')
            break
    else:
        remain_time = remain_time - 1
        print('輸入錯誤! 還有',remain_time, '次機會')
if remain_time == 0:
    print('輸入過多次錯誤 已取消輸入資格')



   

