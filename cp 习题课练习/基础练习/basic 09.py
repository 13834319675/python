# 写一个程序来管理用于登陆系统的用户信息：登陆名字和密码。
# 陆用户账号建立后，已存在用户可以用登陆名字和密码重返系统，
# 新用户不能用别人的用户名建立用户账号

user = {"chenpeng":123456,"zhangsan":111111,"lisi":666666}

def creat_user(username,password):
# 建立账号名和密码,如果账户纯在则提示,不存在则创建

    usernames = user.keys()
    if username in usernames:
        print("用户名已被注册了!")
    else:
        user[username] = password
        print("恭喜你!注册成功1")

creat_user("pengpeng",123456)
print(user)

def login_user(username,password):
    usernames = user.keys()
    if username in usernames:
        print("用户名验证成功!")
        if password == user[username]:
            print("登录成功1")
        else:
            print("你唱歌蠢货,密码都记不住!")
    else:
        print("你不是我们的会员!")

login_user("chenpen",123456)