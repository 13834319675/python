import threading

sum = 0
loopsum = 1000000

def MyAdd():
    global sum ,loopsum

    for i in range(1,loopsum):
        sum = sum+1
    print("第{0}次相加的结果为{1}".format(loopsum,sum))

def MyMin():
    global sum,loopsum
    for i in range(1,loopsum):
        sum = sum-1
    print("第{0}次相减的结果为{1}".format(loopsum, sum))

if __name__ == '__main__':
    print("Starting ....{0}".format(sum))

    # 开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=MyAdd, args=())
    t2 = threading.Thread(target=MyMin, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done .... {0}".format(sum))


