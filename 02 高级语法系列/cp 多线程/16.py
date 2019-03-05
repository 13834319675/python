import time
import threading

semaphore = threading.Semaphore(3)

def func():
        semaphore.acquire()
        for i in range(3):
            print(threading.current_thread().getName()+" get semaphore")

        time.sleep(10)
        semaphore.release()
        print(threading.current_thread().getName()+" release semaphore")

for i in range(8):
    t1 = threading.Thread(target=func,args=())
    t1.start()

# 允许同事有几个线程使用资源