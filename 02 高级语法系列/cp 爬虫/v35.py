from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rep = request.urlopen(url)
content = rep.read()

soup = BeautifulSoup(content,"lxml")
print(soup.prettify())
print("=="*20)
print(soup.select("title")[0])
print("=="*20)
print(soup.select("meta[content='always']")[0])
