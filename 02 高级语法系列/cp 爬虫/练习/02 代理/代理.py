"""
构建代理服务器队列
构建访问服务器,随机抽取一个代理
抽取可用,randint.choice
"""
"""
分析步骤
构建代理群
每次访问 随机抽取代理并执行
"""
from urllib import request,error
import random

# 构建代理步骤
# 1,设置代理地址
proxy_list = [
# 列表中存放的是dict类型的元素
    {"http": "101.50.1.2:80"},
    {"http": "58.240.172.110:3128"},
    {"http": "124.193.51.249:3128"},
    {"http": "120.199.64.163:8081"}
]
# 创建请求头 proxyHeadler
proxy_headler_list = []
for proxy in proxy_list:
    proxy_headler = request.ProxyHandler(proxy)
    proxy_headler_list.append(proxy_headler)
# 创建opener
opener_list = []
for proxy_headler in proxy_headler_list:
    opener = request.build_opener(proxy_headler)
    opener_list.append(opener)

# 现在访问url使用代理服务器
url = "http://www.baidu.com"
try:
    # 安装opener
    opener = random.choice(opener_list)
    request.install_opener(opener)

    # 请求
    req = request.urlopen(url)
    rsp = req.read().decode()
    print(rsp)
except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)