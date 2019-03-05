import time
import threading

metux = threading.RLock()
num = 1

class MyTherad(threading.Thread):
    def run(self):
        global num
        time.sleep(1)


        if metux.acquire(1):
           num = num +1
           msg = self.name +"set num to "+str(num)
           print(num)
           print(msg)
           metux.acquire()

           metux.release()
           metux.release()

def func():
    for i in range(8):
        t = MyTherad()
        t.start()

if __name__ == '__main__':
    func()


