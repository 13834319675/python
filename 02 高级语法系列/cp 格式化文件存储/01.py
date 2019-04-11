import xml.dom.minidom
# 负责解析xml文件

from xml.dom.minidom import parse

# 使用minidom打开xml文件
DOMtree = xml.dom.minidom.parse("student.xml")
#得到文件对象
doc = DOMtree.documentElement

# 显示子元素
for ele in doc.childNodes:                                      # 将得到的xml对象利用for循环 获取艮节点的对象
    print(type(ele),"是这个类型")
    if ele.nodeName == "Teacher":
        print("----Node:{0}----".format(ele.nodeName))          # 判断挑选匹配的节点
        childs = ele.childNodes
        #print(childs)
        for child in childs:                                    # 利用first循环获取所有属性
            if child.nodeName == "Name":                        # 判断是否匹配
        # date是文本节点的属性 表示他的值
                print("Name:{0}".format(child.childNodes[0].data)) #
            if child.nodeName == "Mobile":
                print("Mobile:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Age_1":
                # data是文本节点的一个属性，表示他的值
                print("Age_1: {0}".format(child.childNodes[0].data))
                if child.hasAttribute("detail"):
                    print("Age-detail: {0}".format(child.getAttribute("detail")))

    else:
        print("Student{0}".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                # date是文本节点的属性 表示他的值
                print(" Student Name:{0}".format(child.childNodes[0].data))

            if child.nodeName == "Age":
                print("Student Age:{0}".format(child.childNodes[0].data))


