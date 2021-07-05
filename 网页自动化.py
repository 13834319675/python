from selenium import webdriver
from PIL import Image
import pytesseract
import time

driver = webdriver.Edge("C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
driver.implicitly_wait(5)#设置超时时间
driver.maximize_window()#窗口最大化显示
driver.get("http://sx.12348.gov.cn/duty/auth/login")
send_name = driver.find_element_by_class_name("right_input").send_keys("15935061198")
send_password = driver.find_element_by_name("_password").send_keys("Sfj123456@")
#img = driver.find_element_by_xpath("/html/body/div/form/div[2]/div[3]/ul/li[3]/a/img").location
img = driver.find_element_by_class_name("code_img")
location = img.location
size = img.size
print(location,size)
#print(img,img1)
driver.save_screenshot("pictures.png")
page_snap_obj = Image.open("pictures.png")
left = location['x']
top = location['y']
print(left,top)
right = left + size['width']
bottom = top + size['height']
# 切割验证码
image_obj = page_snap_obj.crop((left, top, right, bottom))
image_obj.show()
time.sleep(5)
#转灰度
img = image_obj.convert("L")
pixdata = img.load()
print(img.size)






#result = pytesseract.image_to_string(image_obj)

#print(result)

