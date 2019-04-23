#编写一个程序，求 100~999 之间的所有水仙花数
#如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数

for i in range(100,1000):
    teep = list(str(i))
    a = int(teep[0])
    b = int(teep[1])
    c = int(teep[2])

    if a**3+b**3+c**3==i:
        print(i)
print(type(a))

# 三色球问题
#有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。
# 先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，
# 编程计算摸出球的各种颜色搭配。
for red in range(0,4):
    for yello in range(0,4):
        for green in range(2,7):
            if red+yello+green==8:
                print("red:{0}".format(red))
                print("yello{0}".format(yello))
                print("green{0}".format(green))