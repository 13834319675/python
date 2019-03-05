import time
import threading

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func1():
    print("func1 starting,,,")
    lock_1.acquire(timeout=4)
    print("func1 申请了 lock_1")
    time.sleep(2)
    print("lock_1 等待 lock_2")

    rst = lock_2.acquire(timeout=4)
    if rst:
        print("func1 已经得到了lock_2")
        lock_2.release()
        print("func1 已经释放了lock_2")
    else:
        print("func1 什么也没有申请到")

    lock_1.release()
    print("func1 释放了 lock_1")

    print("func1 done")

def func2():
    print("func2 starting,,,")
    lock_2.acquire()
    print("func2 申请了 lock_2")
    time.sleep(6)
    print("func2 等待 lock_1")

    lock_1.acquire()
    print("func2 申请 lock_1")

    lock_1.release()
    print("func2 释放 lock_1")

    lock_2.release()
    print("func2 释放 lock_2")

    print("func2 done")

if __name__ == '__main__':
    print("程序开始")
    t1 = threading.Thread(target=func1,args=())
    t2 = threading.Thread(target=func2,args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("程序执行结束")
