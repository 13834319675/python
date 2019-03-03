import threading


lock = threading.Lock()


import threading

sum=0
loopsum=10

def myAdd():
    global  sum, loopSum
    for i in range(1, loopsum):
        # 上锁，申请锁
        lock.acquire()
        sum += i # sum+=1
        # 释放锁
        lock.release()
        print("第{0}次相加的结果为{1}".format(i, sum))

def myMinu():
    global  sum, loopSum
    for i in range(1, loopsum):
        lock.acquire()
        sum -= i  # sum-=1
        lock.release()
        print("第{0}次相相减的结果为{1}".format(i, sum))
if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))
