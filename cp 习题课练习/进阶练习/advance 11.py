"""
创建北京和成都两个校区
创建Linux\Python两个课程
创建北京校区的Python 3期课程和成都校区的Linux 1期课程
管理员创建了北京校区的学员小张，并将其分配在了Python 3期
管理员创建了讲师小周，并将其分配给了Python 3期
讲师小周创建了一条 Python 3期的上课记录 Day02
讲师小周为Day02 这节课所有的学院批改了作业， 小张得了A，小王得了B
学员小张查看了自己所报的课程
学员小张在 查看了 自己在Python 3 的成绩列表然后退出了
学院小张给了讲师小周好评"""
Course_list = []

class School():
    def __init__(self,school_name):
        self.school_name = school_name
        self.Student_list = []
        self.Teacher_list = []
        global Course_list
    # hire(聘用)
    def hire(self,obj):
        self.Teacher_list.append(obj.name)
        print("我们现在聘用了了一位新老师".format(obj.name))
    # enroll(参加,注册)
    def enroll(self,obj):
        self.Student_list.append(obj.name)
        print("我们又来了一位新学员".format(obj.name))

# grade(年级) grade_code(年级代码),grade_course(年级课程) members 成员
class Grade(School):
    def __init__(self, school_name, grade_code, grade_course):
        super(Grade, self).__init__(school_name)
        self.code = grade_code
        self.course = grade_course
        self.members = []
        Course_list.append(self.course)

        print("我们现在有了在{}学习{}年级{}课程的同学".format(self.school_name, self.code, self.course))

    def course_info(self):
        print("课程大纲是{0}".format(self.course))

Python = Grade("电大",3,"python")
Python.course_info()
Linux = Grade("山大",4,"linux")
Linux.course_info()
# member成员
class School_member():
    def __init__(self,name,age,sex,role):
        self.name = name
        self.age = age
        self.sex = sex
        self.role = role
        self.course_list = []

        print("我叫{},今年{}了,性别{},是一个{}"
              .format(self.name,self.age,self.sex,self.role))

Stu_nun_id = 00
class Students(School_member):
    def __init__(self,name,age,sex,role,course):
        super(Students, self).__init__(name,age,sex,role)
        global Stu_nun_id
        Stu_nun_id+=1
        stu_id = course.school_name+"S"+str(course.code)+str(Stu_nun_id).zfill(2)
        # zfill 填充的作用，当只有一位数时前面填充0， 只能对str类型做操作

        self.id = stu_id
        self.mark_list = {}

    def study(self,course):
        print("我来这里学{}课的,我的学号是{}".format(course.course,self.id))

    def pay(self,course):
        print("我交了1000块钱学{}".format(course.course))

    def praise(self,obj):
        print("{}觉得{}课真棒".format(self.name,obj.name))

    def mark_check(self):
        for i in self.mark_list.items():
            print(i)

    def out(self):
        print("我离开了")
tea_nun_id = 00
class Teacher(School_member):
    def __init__(self,name,age,sex,role,course):
        super(Teacher, self).__init__(name,age,sex,role)
        global tea_nun_id
        tea_nun_id+=1

        tea_id = course.school_name+"T"+str(course.course)+str(tea_nun_id).zfill(2)
        self.tea_id =tea_id

    def teac(self,course):
        print("我是来{}学校讲{}课程的,我的id是{}".format(course.school_name,course.course,str(self.tea_id)))

    def record_mark(self,Data,course,obj,level):
        obj.mark_list["Data"+Data] = level

a = Students("小王",18,"男","学生",Python)
Python.enroll(a)
a.study(Python)
a.pay(Python)

b = Students("小李",20,"女","学生",Linux)
Linux.enroll(b)
a.study(Linux)
a.pay(Linux)

t =Teacher("小周",30,"M","teacher",Python)
Python.hire(t)
t.teac(Python)
t.record_mark('1',Python,a,"A")
t.record_mark("1",Python,b,"B")
t.record_mark('2',Python,a,"A")
t.record_mark("2",Python,b,"A")
print("小王查看了自己的课程")
print(b.course_list)
print("小王查看了自己的成绩")
b.mark_check()
print("小王退出了")
b.out()
print("给好评")
a.praise(t)

