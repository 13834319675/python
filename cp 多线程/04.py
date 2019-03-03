import time
import threading

def loop1(in1):
    print("Start loop1 at:",time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("End loop1 at:",time.ctime())

def loop2(in1, in2):
    print('Start loop2 at :', time.ctime())
    print("我是参数 " ,in1 , "和参数  ", in2)
    time.sleep(2)
    print('End loop2 at:', time.ctime())

def main():
    print("Starting at:",time.ctime())
    t1 = threading.Thread(target=loop1,args=("隔壁老王",))
    t1.start()
    t2 = threading.Thread(target=loop2,args=("小明","悦悦"))
    t2.start()
    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
    # 一定要while语句
    # 因为启动线程后本程序作为主线程存在
    # 如果主线程执行完毕，则子线程可能需要终止
    while True:
        time.sleep(10)
