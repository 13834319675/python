# 输入一个整数,与随机产生的整数进行比较

import random
teep = input("请输入0-10之间任意的整数:")

rand = random.randint(1,10)
n = 0
while n<3:
    if teep.isdigit():
        teep = int(teep)
        if teep>rand:
            teep = input("大了,请重新输入:")
        elif teep==rand:
            print("答对了!")
            break
        else:
            teep = input("小了,请重新输入:")

    else:
        print("输入错误")
        teep = input("请输入整数:")
    n = n+1
print("正确答案为{0}".format(rand))
print("结束")
