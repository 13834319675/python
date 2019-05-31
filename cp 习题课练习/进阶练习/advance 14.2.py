"""
写一个用户登录验证程序，文件如下 1234.json

1234.json
{"expire_date":"2021-01-01","id":"1234","status":0,"pay_day":22,"password":"abc"}

- 用户名为json的文件名
- 判断是否过期，与expire_date做比较
- 登陆成功后打印登陆成功，三次登陆失败，status值改为1，并且锁定账号
"""
import os
import time
import json

count = 0

while count<3:
    user = input("请输入同户名:")
    f = user.strip()+".json" # 去除空格进行字符串拼接

    if os.path.exists(f): # 检测文件是否存在
        fs = open(f,"r+",encoding="utf-8")# 打开json文件
        j_user = json.load(fs) # 把json文件内容赋值给j_user
        print(j_user)
        if j_user["status"] == 1:
            print("账号已被锁定")
            break

        else:
            expire_dt = j_user["expire_date"]
            current_st = time.time()
            expire_st = time.mktime(time.strptime(expire_dt,"%Y-%m-%d"))
            print(expire_dt,current_st,expire_st)

            if current_st>expire_st:
                print("账号已过期")
                break
            else:
                while count<3:
                    pwd = input("请输入密码:")
                    if pwd.strip() == j_user["password"]:
                        print("登陆成功")
                        break
                    else:
                        if count ==2:
                            print("密码已经重复输错三次,账户将被销毁")
                            j_user["status"] =1
                            fs.seek(0)
                            fs.truncate()
                            fs.close()
                    count +=1

    else:
        print("账号不存在")
        count += 1
        break



