import math,random

num = input('请输入一个三位数：')

# 输入的数是字符型，需要转换为整形，不然会报错
# isdigit() 检测数字是否存数字
if num.isdigit():
    if 1 <= int(num) <= 100:
        print(num)
    else:
        print("请安规定输入！")
else:
    print('输入错误')


# 练习判断输入的一个数和系统随机数做比较！
# 明天继续，加油 ^_^！