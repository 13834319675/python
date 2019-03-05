import threading

sum=0
loopsum=10
lock = threading.Lock
def myadd():
    global sum, loopsum
    for i in range(1,loopsum):
        # 上锁，申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()
        print("第{0}次相加的结果为{1}".format(i,sum))

def mymin():
    global sum,loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum -= 1
        lock.release()
        print("第{0}次相加的结果为{1}".format(i, sum))
def main():
    global sum
    print("Starting at:{0}".format(sum))
    t1 = threading.Thread(target=myadd,args=())
    t2 = threading.Thread(target=mymin,args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Done at：{0}".format(sum))
if __name__ == '__main__':
    main()



