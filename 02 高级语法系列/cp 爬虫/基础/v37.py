from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 需要使用的浏览器
driver  = webdriver.Chrome()
url = "http://www.baidu.com"

driver.get(url)

text = driver.find_element_by_id("wrapper").text
print(text)
print("--"*20)
print(driver.title)

# 得到页面的快照
driver.save_screenshot("快照.png")
# id="kw" 的是百度的输入框，我们得到输入框的ui元素后直接输入“大熊猫"
driver.find_element_by_id("kw").send_keys(u"今日头条")

# id="su"是百度搜索的按钮，click模拟点击
driver.find_element_by_id("su").click()
driver.save_screenshot("今日头条.png")
time.sleep(5)

# 获取当前页面的cookie
print(driver.get_cookies())
# 模拟输入两个按键ctrl a
# 模拟输入两个按键 ctrl+ a
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
#ctr+x 是剪切快捷键
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')


driver.find_element_by_id("kw").send_keys(u"航母")
driver.save_screenshot("航母.png")

driver.find_element_by_id("kw").send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot("航母2.png")

# 清空输入框
driver.find_element_by_id("kw").clear()
driver.save_screenshot("clear.png")

# 关闭浏览器
driver.quit()
