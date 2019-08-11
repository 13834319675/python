"""
URlERROR的使用
"""

from urllib import request,error

if __name__ == '__main__':
    url = "http://www.baidu"

    try:
        rep = request.Request(url)  # 创建requests实例
        rsp = request.urlopen(rep)  # 用URLopen打开
        html = rsp.read().decode()  # 读取解码
        print(html)
    except error.URLError as e:
        print("URLError {0}".format(e))
        print("URLError {0}".format(e.reason))

    except Exception as e:
        print(e)