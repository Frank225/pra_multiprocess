from multiprocessing import Process
import os
import time
from time import sleep



def run_c(name, age, **kwargs):
    for i in range(10):
        print('zijincheng', name, age, os.getpid())
        print(kwargs)
        sleep(0.2)

if __name__ == '__main__':
    p = Process(target=run_c,args=('ffff',18),kwargs={'m':20})
    p.start()
    sleep(1)
    p.terminate()
    p.join()
