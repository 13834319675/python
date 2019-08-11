"""
URLError的使用
"""
from urllib import request, error

if __name__ == '__main__':
    url1 = "http:iiiiiiiiidu//www.baidu.com/welcome.html"

    url2 = "http://www.sipo.gov.cn/www"
    try:
        rep = request.Request(url2)
        rsp = request.urlopen(rep)
        heml = rsp.read().decode()
        print(heml)
    except error.HTTPError as e:
        print("URLError {0}".format(e))
        print("URlError {0}".format(e.reason))

    except error.URLError as e:
        print("URKError {0}".format(e))
        print("URlError {0}".format(e.reason))

    except Exception as e:
        print(e)

