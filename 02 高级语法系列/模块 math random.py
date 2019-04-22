import math

# print(math)
print(math.ceil(5.1))
print(math.ceil(5.9))#向上取整

# floor 乡下取整操作
print(math.floor(5.5))
import keyword

print(keyword.kwlist) #系统保留

# round() 四舍五入操作

print(round(5.45))
# sqrt 平开方 ，返回浮点数
print(math.sqrt(9))

# pow() 与幂运算差不多，计算一个数的几次方
print(math.pow(4,3))# 返回浮点型
print(4**3) # 返回整形

# fabs() 对一个数获取绝对值
print(math.fabs(-1.20)) # 返回浮点数

# abc()返回值有本身类型而定
print(abs(-1.1)) #获取绝对值操作，菲math模块，是python内置函数

# sum() python中的求和
print(sum([1,4.5,20.2]))
# fsum() math模块中的求和
print(math.fsum([1,4,5,7,9]))

# math.modf() 讲一个浮点数拆分为整数部分和小树部分
# 返回一个元祖
print(math.modf(-1.1))

# copysign() 将第二个数的符号正负，传给第一个数
print(math.copysign(10,-20))

# 打印自然对数e和pi的
print(math.e)
print(math.pi)

# 随机数模块
import random
# random() 创建0-1的随机数，包括0不包括1

for i in range(10):
    print(random.random())
# 随机出现一个指定范围内的值
print(random.randint(1,10))

# random.randrange() 获取指定范围的值，可以指定间隔
print(random.randrange(1,9,3))

# choice() 随机获取列表中的值
print(random.choice([1,5,7,100,50]))

# shuffle() 随机打乱序列,返回值是None
list1 = [1,3,5,7,9,10]
print(list1)
list2 = random.shuffle(list1)
print(list1)

# uniform() 随机获取指定范围内的值（包括小树）
print(random.uniform(1,10))

# 小案例 math
