# 需要导入相应的包ftplib
import ftplib
import os
import time

# 三部分精确表示在ftp服务器上的某一个文件
# 好多公开的ftp服务访问会出错或者没有反应
HOST = "ftp.acc.umu.se"
DIR = 'Public/EFLIB/'
FILE = 'README'

# 1,客户端链接远程主机上的FTp服务器
try:
    f = ftplib.FTP()
    # 通过设置调试级别可以方便调试
    f.set_debuglevel(2)
    # 链接主机地址
    f.connect(HOST)

except Exception as e:
    print(e)
    exit()
print("connected to host {0}".format(HOST))

# 2, 客户端输入同户名和密码(或者anonymous和电子邮件地址)
try:
    # 登录(login)如果要输入用户名信息,则默认视同匿名登录
    f.login()

except Exception as e:
    print(2)
    exit()
print("Logged in as 'anonymous'")

# 3, 哭护短和服务器进行各种文件传输和信息查询操作
try:
    #更改当前目录到指定目录
    f.cwd(DIR)

except Exception as e:
    print(e)
    exit()
print("changed dir to {0}".format(DIR))

try:
    # 从服务器上下载文件
    # 第一个参数是ftp命令
    # 第二个参数是会掉函数
    # 此函数的意思是 执行REtR命令,下载文件到本地,运行回调函数
    f.retrbinary('RETT {0}'.format(FILE),open(FILE,"wb").write())
except Exception as e:
    print(2)
    exit()

# 4,客户端从远程服务器退出 结束传输
f.quit()