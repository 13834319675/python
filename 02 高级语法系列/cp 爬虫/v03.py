import urllib
import requests


url = "https://egame.qq.com/497383565?ADTAG=zd-liveplug&adtag=qqbrowser.zbzs"

rsp = urllib.request.urlopen(url)

html = rsp.read()
html = html.decode("utf-8")

print("URl:{}".format(rsp.geturl()))
print("INFo:{}".format(rsp.info()))
print("CODE:{}".format(rsp.getcode()))