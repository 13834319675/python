import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        super(ClockProcess,self).__init__()
        self.interval=interval

    def run(self):
        num = 0
        while True:
            num = num+1
            print("frist {0} the time is {1}".format(num,time.ctime()))
            time.sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    while True:
        print('sleeping.......')
        time.sleep(1)