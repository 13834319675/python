from urllib import request,parse
from http import cookiejar

# 创建cookie吉安人实例
cookie  =  cookiejar.CookieJar()
# 生成cookiejar管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handle = request.HTTPHandler()
# 创建https请求管理器
https_handle = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(cookie_handle,http_handle,https_handle)

def login():
    """
    负责初次登陆
    输入用户名密码
    获取cookie
    :return:
    """
    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"
    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email": "13119144223",
        "password": "123456"
    }
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url,data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)

if __name__ == '__main__':
    login()
    """
    执行login之后,会得到授权过的login
    我们尝试把cookie打印出来
    """
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
