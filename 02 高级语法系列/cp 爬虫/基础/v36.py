# 通过webdriver操作网页
from selenium import webdriver
import time
# 通过key模拟键盘
from selenium.webdriver.common.keys import  Keys

# 操作哪个浏览器就对哪个浏览器建一个实例
# 自动按照环境变量查找相应的浏览器
driver = webdriver.PhantomJS()

# 如果浏览器没有在相应环境变量中，需要指定浏览器位置

driver.get("http://www.baidu.com")

print(driver.title)