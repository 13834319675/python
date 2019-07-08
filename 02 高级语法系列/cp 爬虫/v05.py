"""
利用parse模块模拟post请求
分析百度词典
分析步骤
1.打开f12
2.尝试输入单词girl,发现每隔一个字符都有请求
3.请求地址是,https://fanyi.baidu.com/sug
4.利用NetWork-All-Hearders,查看,发现FromData的值是,kw:girl
5.检查返回内容的格式,发现返回的是json格式的内容==>需要使用json模块
"""
from urllib import request,parse
# 负责处理json格式的模块
import json

"""
大致流程是:
1.利用data构建内容,然后URLopen打开
2.返回一个json格式的结果
3.结果应该就是girl的释义
"""
translated = input("Please enter the content to be translated:")
baseurl = "https://fanyi.baidu.com/sug"
# 存储用来模拟from的数据一定要用dict格式
data = {
    'kw':translated
}
# 需要使用data模块对data进行编码
# 先把data的数据转换为二进制在进行编码
data = parse.urlencode(data).encode("utf-8")
print(data)
print(type(data))

# 我们需要构建一个请求头,请求的头部至少包含content-length
# request要求传入的请求是一个dict模式
headers = {
    'Content-length':len(data)
}

# 有了 headers,data,url 就可以尝试发送请求了
rsp = request.urlopen(baseurl,data=data)

json_data = rsp.read().decode("utf-8")
print(json_data)
print(type(json_data))

# 把json字段转化成字符串
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data["data"]:
    print(item['k'],"--",item['v'])