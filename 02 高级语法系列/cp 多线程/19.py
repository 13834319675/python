import time
import multiprocessing

def clock(interval):
    while True:
        print("the time is %s"%time.ctime())
        time.sleep(interval)


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock,args=(2,))
    p.start()

    while True:
        print("sleeping,,,")
        time.sleep(1)

# 进程
