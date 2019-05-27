# 编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
# 定义一个异常
def sub(a,b):
    if a<b:
        raise Exception("被减数不能小于减数")

try:
    sub(1,3)
except Exception as e:
    print("好像出错了{}".format(e))
    