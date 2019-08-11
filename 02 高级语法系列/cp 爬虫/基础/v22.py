'''
使用参数headers和params
研究返回结果

'''
import requests
# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"

kw = {
    "wd":"隔壁老王"
}
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
}
rep = requests.get(url=url,params=kw,headers=headers)

print(rep.text)
print(rep.content)
print(rep.url)
print(rep.encoding)
print(rep.status_code) # 请求返回码
