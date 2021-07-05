from selenium import webdriver
from PI import Image
import base64
import requests
import time

def baidu_api(Verification_code, AK, SK):#Verification_code验证码路径,AK,SK百度云的身份识别码
    chrome.get_screenshot_as_file('reg.png')  # 获取登陆页面的图片
    code_img = chrome.find_element_by_xpath(Verification_code)  # 找到验证码图片的位置
    img = Image.open('reg.png')# 保存图片
    c_img = img.crop((code_img.location['x'], code_img.location['y'], code_img.location['x'] + code_img.size['width'],
                      code_img.location['y'] + code_img.size['height']))  # 截取验证码图片
    c_img.save('reg_code.png')
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
            'client_id='+AK+'&' \
            'client_secret='+ SK
    response = requests.get(host)
    token = response.json()['access_token']
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    f = open('reg_code.png', 'rb')# 二进制方式打开图片文件
    img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    dict_a = response.json()['words_result']
    if response:
        dict_a = eval(str(dict_a)[1:-1])#数据类型的格式转换
        dict_a = dict(dict_a)#转化为字典类型
        dict_a = dict_a['words']
        dict_a = "".join(dict_a.split())  # 使用一个空字符串合成列表内容生成新的字符串
        dict_a = dict_a.lower()#把大写字母改为小写字母
        return dict_a
    else:
        chrome.refresh()

chrome = webdriver.Chrome()#浏览器实例化
chrome.maximize_window()#最大化浏览器
chrome.get('自己登陆的网址')
test = baidu_api("/html/body/div/form/div[2]/div[3]/ul/li[3]/a/img", 'm8N1rszBjK4Cg84LyEktNcjI', 'DWA323C5OkApYurmlgzmrtvqpSMZUSRh')#返回识别的验证码
chrome = webdriver.Chrome()
print(test)#验证码
