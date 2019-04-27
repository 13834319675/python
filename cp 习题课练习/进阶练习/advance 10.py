#定义一个学生类，有下面的类属性
#姓名
#年龄
#成绩（语文，数学，英语）每课成绩类型为整数 类方法：
#获取学生的姓名：get_name() 返回类型：str
#获取学生的年纪：get_age()返回类型：int
#返回3门科目中最高的分数，get_course()返回类型：int#

class Student():
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return str(self.name)

    def get_age(self):
        return int(self.age)

    def max_score(self):
        return int(max((self.score)))

stu = Student("张三",18,[80,99,66])

print(stu.name,stu.age,stu.score)
print(stu.get_name(),stu.get_age(),stu.max_score())