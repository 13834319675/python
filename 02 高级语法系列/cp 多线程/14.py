import time
import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func1():
    print("func1 Starting,,,")
    lock_1.acquire()
    print("func1 申请了 lock_1")
    time.sleep(2)
    print("func1 等待 lock_2")
    lock_2.acquire()
    print("func1 申请了 lock_2")

    lock_2.release()
    print("func1 释放了 lock_2")
    lock_1.release()
    print("func1 释放了 lock_1")

    print("func1 done")

def func2():
    print("func2 Starting,,, ")
    lock_2.acquire()
    print("func2 申请了lock_2,,,")
    time.sleep(4)
    print("func2 等待 lock_1,,,")
    lock_2.acquire()
    print("func2 申请了 lock_2")
    lock_1.release()
    print("func2 释放了 lock_1")
    lock_2.release()
    print("func2 释放了 lock_2")

    print("func2 done")

if __name__ == '__main__':
    print("主程序启动")

    t1 = threading.Thread(target=func1,args=())
    t2 = threading.Thread(target=func2,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("执行结束")

