import time
import threading

def loop1():
    print("start loop1 at:",time.ctime())
    time.sleep(6)
    print("end loop1 at:",time.ctime())

def loop2():
    print("start loop2 at:",time.ctime())
    time.sleep(1)
    print("end loop2 at:",time.ctime())

def loop3():
    print("start loop3 at:",time.ctime())
    time.sleep(5)
    print("end loop3 at:",time.ctime())

def main():
    print("Starting at:",time.ctime())
    t1 = threading.Thread(target=loop1,args=()) # 生成一个threading.Thread实例
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2,args=())
    t2.setName("THR_2")
    t2.start()


    t3 = threading.Thread(target=loop3,args=())
    t3.setName("THR_3")
    t3.start()

    # 预测3秒后 t2 线程将结束
    time.sleep(3)
    # enumerate 得到正在运行的子线程，即线程1和线程3
    for thr in threading.enumerate():
        print("正在运行的线程的名字是:{0}".format(thr.getName()))
    print("正在运行的子线程的数量为{0}".format(threading.activeCount()))
    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)




