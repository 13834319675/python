"""
自己定义一个异常类，继承Exception类, 捕获下面的过程：判断输入的字符串长度是否小于5
"""

class MyErro(Exception):
    def __init__(self,str1):
        self.str1 = str1

    def process(self):
        if len(self.str1)<5:
            print("字符串的长度必须大于5")

        else:
            print("算你聪明")
try:
    erro  = MyErro("123")
    erro.process()
except MyErro as e:
    print("错误,{}".format(e))