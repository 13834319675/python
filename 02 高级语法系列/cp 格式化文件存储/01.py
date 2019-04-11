import xml.dom.minidom
# 负责解析xml文件

from xml.dom.minidom import parse

# 使用minidom打开xml文件
DOMtree = xml.dom.minidom.parse("student.xml")
#得到文件对象
doc = DOMtree.documentElement

# 显示子元素
for ele in doc.childNodes:
    #print(ele)
    if ele.nodeName=="Teacher":
        print("----Node:{0}----".format(ele.nodeName))
        childs = ele.childNodes
        #print(childs)
        for child in childs:
            if child.nodeName == "Name":
        # date是文本节点的属性 表示他的值
                print("Name:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Mobile":
                print("Mobile:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Age_1":
                # data是文本节点的一个属性，表示他的值
                print("Age_1: {0}".format(child.childNodes[0].data))
                if child.hasAttribute("detail"):
                    print("Age-detail: {0}".format(child.getAttribute("detail")))



