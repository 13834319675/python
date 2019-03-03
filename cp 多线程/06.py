import time
import threading

def fun():
    print("start fun:")
    time.sleep(2)
    print("end fun")

print("main therad")

t1 = threading.Thread(target=fun,args=())
t1.start()
t1.join()
time.sleep(1)
print("main therad end")