import xml.etree.ElementTree as et

tree = et.parse(r'to_edit.xml')

#解析xml文件
#获取文件对象赋值给root
#循环获取 xml文本的所有节点和属性

root = tree.getroot()

for e in root.iter():
    print(e.text,e.tag)

for stu in root.iter('Student'):
    name = stu.find('Name')

    if name != None:
        name.set( 'test', name.text * 3)

stu = root.find('Student')

#生成一个新的 元素
e = et.Element('ADDer')
e.attrib = {'a':'b'}
e.text = '我加的'

stu.append(e)
print("/")
e1 = et.Element("year")
e1.attrib={"data":"2019"}
e1.text="今年是"
stu.append(e1)
# 一定要把修改后的内容写回文件，否则修改无效
tree.write(r'to_edit.xml')
