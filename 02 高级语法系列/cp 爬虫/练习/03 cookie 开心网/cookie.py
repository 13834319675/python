"""
登陆开心网
利用cookie
免除ssl验证
"""
from urllib import request,parse
import ssl
'''
步骤：
1， 寻找登录入口， 通过搜查相应文字可以快速定位
  login_url = "https://security.kaixin001.com/login/login_post.php"
  相应的用户名和密码对应名称为email, password
2. 构造opener
3. 构造login函数
'''
#怒略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

from http import cookiejar

cookie = cookiejar.CookieJar()
cookie_headler = request.HTTPCookieProcessor(cookie)
http_headler = request.HTTPHandler()
https_headler = request.HTTPSHandler()
opener = request.build_opener(cookie_headler,http_headler,https_headler)

def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"
    data = {
        "email": "13119144223",
        "password": "123456"
    }

    data = parse.urlencode(data).encode()
    # http请求头
    headers = {
        "Content-Length": len(data),
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }
    # 构建Request请求
    req = request.Request(login_url,data=data,headers=headers)
    rsp = opener.open(req)
    http = rsp.read().decode()

def GetHomePAge():
    base_url = "http://www.kaixin001.com/home/?_profileuid=181697221"
    req = opener.open(base_url)
    rsp = req.read().decode()
    print(rsp)

if __name__ == '__main__':
    login()
    GetHomePAge()


