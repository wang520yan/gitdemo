 # -*- encoding:utf-8 -*-
import os
import random
from multiprocessing import Process,Queue
import time

# 进程间通信
def write(q):
    print('Process to write: %s' % os.getpid())   # os.getpid() 获取当前进程的进程号
    print(os.getppid())   # 获取父进程号
    for value in ['A', 'B', 'C']:
        print('put %s to queue ...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('process to read : %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)

if __name__ == '__main__':
    q = Queue()
    Pw = Process(target=write, args=(q, ))
    Pr = Process(target=read, args=(q,))
    Pw.start()     # 启动进程
    Pr.start()
    Pw.join()     # 等待子进程结束后继续往下，用于进程同步
    Pr.terminate()