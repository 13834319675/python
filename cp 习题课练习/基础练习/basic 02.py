# 给定一个程序,判断输入的年份是否为闰年

teep = int(input("请输入一个年份:"))
if teep%4 == 0:
    print("{0}年份是闰年!".format(teep))
else:
    print("{0}年不是闰年".format(teep))
print("结束")

# 方法二

year = input("请输入年份:")

if year.isdigit():
    year = int(year)
    if year%4 == 0:
        print("{0}年是闰年!".format(year))
    else:
        print("{0}年不是闰年".format(year))
else:
    print("输入错误,请输入年份!")
print("结束")