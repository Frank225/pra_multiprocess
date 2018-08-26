from multiprocessing import Process
import os
import time


nums = [11,22]

def work1():
    '''子进程'''
    print('zijinc1')
    for i in range(3):
        nums.append(i)
        time.sleep(1)
        print('pid',os.getpid(),nums)

def work2():

    print(os.getpid(),nums)

if __name__ == '__main__':
    p1 = Process(target=work1)
    p1.start()
    # 等join
    p1.join()

    p2 = Process(target=work2)
    p2.start()
    # p2.join()