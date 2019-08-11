from lxml import etree

html = etree.parse("./v30.html")
print(type(html))

rst = html.xpath('//nook')
print(type(html))
print(rst)

# xpath的意识是，查找带有category属性值为sport的book元素

rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

rst = html.xpath('//book[@category="sport"]/year')
for i  in  rst:
    print(i)

rst = rst[0]
print(type(rst))
print(rst)
print("=="*20)
print(rst.tag)
print(rst.text)
