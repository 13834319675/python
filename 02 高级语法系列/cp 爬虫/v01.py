from urllib import request
"""
使用urllib.requsst的模块请求一个网页内容,并把内容打印出来
"""

if __name__ == '__main__':
    url = "https://www.zhaopin.com/"
    # 获取相应页面,并返回
    rsp = request.urlopen(url)
    # 把返回的内容读取出来,读取的内容为bytes
    html = rsp.read()
    print(type(html))
    # 如果想把bytes转换成字符串,需要转码
    html = html.decode("utf-8")
    print(html)