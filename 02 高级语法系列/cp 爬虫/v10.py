"""
使用代理访问百度
"""
from urllib import request,error

if __name__ == '__main__':
    url = "http://www.baidu.com"

    # 使用代理步骤
    # 1.设立代理地址
    proxy = {'http':'120.194.18.90:81'}
    # 2.创建proxyhandler 处理器
    proxy_handler = request.ProxyHandler(proxy)
    # 3.创建Opener 打开器
    operer = request.build_opener(proxy_handler)
    # 4. 安装Opener
    request.install_opener(operer)

    # 现在如果访问url 则使用的事代理服务器
    try:
       
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as  e:
        print(e)
    except Exception as e:
        print(e)