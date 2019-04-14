import json
# 此时Student是一个dict内容 不是json
student = {
    "name":"chenpeng",
    "age":18,
    "mobilr":13834319675
}
print(type(student))

stu_json = json.dumps(student)

print(type(stu_json))
print("JSON对象{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)
