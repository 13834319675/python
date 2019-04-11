import xml.etree.ElementTree

# 使用etree解析xml文件
root = xml.etree.ElementTree.parse("student.xml")
print("利用getiterator访问:")
nodes = root.getiterator()
for node in nodes:
    # 获取所有文本标签
    print("{0}---{1}".format(node.tag,node.text))
# 以上得到所有的xml文件中的节点属性标签

print("利用find和findall方法")
ele_teacher = root.find("Teacher")
print(type(ele_teacher))
print("{0}--{1}".format(ele_teacher.tag,ele_teacher.text))
# 以上查找Teacher标签

ele_stu = root.findall("Student")
print(type(ele_stu))
for ele in ele_stu:
    print("{0}--{1}".format(ele.tag,ele.text))
    for sub in ele.getiterator():
        if sub.tag == "Name":
            if "Other" in sub.attrib.keys():
                print(sub.attrib["Other"])
# 获取Student所有的标签属性