from urllib import request,parse
"掌握对url进行编码" \
"需要用到parse模块"

if __name__ == '__main__':
    url = "https://www.baidu.com/s?"

    wd = input("input your keyword:")

    qs = {
        "wd": wd
    }

    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url+qs
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()

    print(html)