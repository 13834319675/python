import time
import threading

loop = [4,2]
class ThreadFunc():
    def __init__(self,name):
        self.name = name

    def loop(self,nloop,nsec):
        print("Start loop",nloop,"at",time.ctime())
        time.sleep(nsec)
        print("Done loop",nloop,"at",time.ctime())

def main():
    print("Starting at: ", time.ctime())

    # ThreadFunc("loop").loop 跟一下两个式子相等：
    # t = ThreadFunc("loop")
    # t.loop
    # 以下t1 和  t2的定义方式相等
    t = ThreadFunc("loop") # ThreadFunc实例化传入的参数loop
    t1 = threading.Thread(target=t.loop, args=("LOOP1", loop[0]))
    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=("LOOP2", loop[1]))
    t1.start()
    t2.start()
    # 常见错误写法
    # t1 = threading.Thread(target=ThreadFunc('loop').loop(100,4))
    # t2 = threading.Thread(target=ThreadFunc('loop').loop(100,2))
    t1.join()
    t2.join()
    print("ALL done at: ", time.ctime())
if __name__ == '__main__':
    main()