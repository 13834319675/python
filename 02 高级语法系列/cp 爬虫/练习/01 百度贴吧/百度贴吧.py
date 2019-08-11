"""
地址"https://tieba.baidu.com/f?ie=utf-8&kw=%E5%89%91%E6%9D%A5&fr=search
    https://tieba.baidu.com/f?kw=%E5%89%91%E6%9D%A5&ie=utf-8
    https://tieba.baidu.com/f?kw=%E5%89%91%E6%9D%A5&ie=utf-8&pn=50
    https://tieba.baidu.com/f?kw=%E5%89%91%E6%9D%A5&ie=utf-8&pn=100
"""
from urllib import request,parse

if __name__ == '__main__':
    qs = {
      "kw":"剑来",
      "ie":"utf-8",
      "pn":0
    }
    urls = []
    baseurl = "https://tieba.baidu.com/f?"
    for i in range(10):
        pn = i*50
        qs['pn'] = str(pn)
        # 拼接网址,并添加到列表
        urls.append(baseurl+parse.urlencode(qs))
    print(urls)
    n=0
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        n = n+1
        print(n)
        f = open("{}.html".format(n),"w",encoding="utf-8")
        f.write(html)
        f.close()
