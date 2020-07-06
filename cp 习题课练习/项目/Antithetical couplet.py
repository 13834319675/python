import json
import urllib3.request

client_id = '****'  # 应用的apiKey
client_secret = '****'  # 应用的secretKey
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
       + client_id + '&client_secret=' + client_secret
request = urllib.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()

if (content):
    content = json.loads(content)
import requests

body = {
    'text': '',
    'index': 0
}
headers = {
    'Content-Type': 'application/json',
}
token = '*****'  # 我的token参数


# function: 获取古诗
def poemGet(keyword):
    body['text'] = keyword
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/poem' + '?access_token=' + token
    param = json.dumps(body).encode('utf-8')
    try:
        result = requests.post(url=url, headers=headers, data=param)
        print(result.json()['poem'][0]['title'])  # 题目
        content = result.json()['poem'][0]['content'].split('\t')
        for i in range(len(content)):
            print(content[i])
    except:
        print('暂时没有找到')


# function: 获取对联
def coupletsGet(keyword):
    body['text'] = keyword
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/couplets' + '?access_token=' + token
    param = json.dumps(body).encode('utf-8')
    result = requests.post(url=url, headers=headers, data=param)
    try:
        result = requests.post(url=url, headers=headers, data=param)
        print(result.json()['couplets']['center'])  # 横批
        print(result.json()['couplets']['first'])  # 上联
        print(result.json()['couplets']['second'])  # 下联
    except:
        print('暂时没有找到')

