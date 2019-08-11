# 利用cookiejar模块获取登陆时的cookie
from urllib import request,parse,error
from http import cookiejar

# 创建cookiejar实例
cookie = cookiejar.CookieJar()

# 生成cookie的管理器
cookie_header = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_header = request.HTTPHandler()
# 生成https管理器
https_header = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_header,https_header,cookie_header)

def login():
    """
    负责初次登陆
    获得登陆凭证cookie
    :return: 
    """
    # 此url需要在登陆状态下form中的action获取
    url = "http://www.renren.com/PLogin.do"

    # 此data需要从登陆的两个from中的input提取属性
    data = {
         "email": "13119144223",
        "password": "123456"
    }
    # 把数据进行转换
    data = parse.urlencode(data).encode()

    # 创建一个请求对象
    req = request.Request(url=url,data=data)

    # 使用opener发送请求
    rsp = opener.open(req)

def getHomePage():
    try:
        url = "http://www.renren.com/965187997/profile"
        # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
        rsp = opener.open(url)

        html = rsp.read().decode()
        with open("html3.html","w") as f:
            f.write(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    login()
    getHomePage()