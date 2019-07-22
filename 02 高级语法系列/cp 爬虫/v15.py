from urllib import request,parse
from http import cookiejar

# 创建Filecookiejar实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename=filename)

# cookie = cookiejar.CookieJar()

cookie_handle = request.HTTPCookieProcessor(cookie)
http_handle = request.HTTPHandler()
https_handle = request.HTTPSHandler()

opener = request.build_opener(cookie_handle,http_handle,https_handle)

def login():
    '''
        负责初次登录
        需要输入用户名密码，用来获取登录cookie凭证
        :return:
        '''

    # 此url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email": "13119144223",
        "password": "123456"
    }
    data = parse.urlencode(data)

    req = request.Request(url,data=data.encode())
    rsp = opener.open(req)

    # 保存cookie到文件
    # ignor_discard表示及时cookie将要被丢弃也要保存下来
    # ignore_expire表示如果该文件中cookie即使已经过期，保存

    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()


