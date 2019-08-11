"""
任务内容和v05一样\
本案例使用request老师实现v05的内容

利用parse模块模拟post请求
分析百度词典
分析步骤
1.f12打开
2.尝试输入单词  返现每一个字符串都有请求
3.请求地址是,"https://fanyi.baidu.com/sug
4.利用NetWork-All-Hearders,查看,返现fromdata是kw:girl  字典格式
5.检查返回内容的格式,发现返回的内容是json格式
"""

from urllib import request,parse

import json
translated = input("Please enter the content to be translate:")
baseurl = "https://fanyi.baidu.com/sug"

data = {
    "kw":translated
}
data = parse.urlencode(data).encode("utf-8")

headers = {
    "Content-Length":len(data)
}

# 构造一个Request实力
#rep = request.urlopen(url=baseurl,data=data)
rep = request.Request(headers=headers,data=data,url=baseurl)
rep = request.urlopen(rep)

json_data = rep.read().decode("utf-8")
print(json_data)

# 把json转换成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item["k"],"--",item["v"])
