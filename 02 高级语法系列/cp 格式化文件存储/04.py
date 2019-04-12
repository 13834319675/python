import xml.etree.ElementTree as et

stu = et.Element("Student1")

name = et.SubElement(stu, 'Name')
name.attrib = {'lang','en'}
name.text = 'maozedong'


age = et.SubElement(stu, 'Age')
age.text = 18

et.dump(stu)

# 获取Student节点 用SubElenent 在Student节点内插入
#attrib属性 和text 用dump写入