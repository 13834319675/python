import time
import threading


class Mythread(threading.Thread):
    def __init__(self,arg):
        super(Mythread,self).__init__()
        self.arg = arg
# 必须重写run函数，run函数代表的是正在执行的功能
    def run(self):
        time.sleep(2)
        print("The args ifor this class is {0}".format(self.arg))

for i in  range(5):
    t = Mythread(i)
    t.start()
    t.join()

print("Main thread is done!!!")


