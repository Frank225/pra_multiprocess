import multiprocessing
from multiprocessing import Process
import os

import time


def run_porc():
    """子进程"""
    # while True:
    #     print('-----2---')
    #     time.sleep(1)
    print('子进程为%d' % os.getpid())
    print('子进程将要结束')

if __name__ == '__main__':
    print('fujincheng', os.getpid())
    p = Process(target=run_porc)
    p.start()