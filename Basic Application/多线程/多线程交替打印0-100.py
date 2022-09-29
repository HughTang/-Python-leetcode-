# 设置N个线程，使其交替打印输出0-100

import threading
import time

def thread1():
    global num
    while num <= 99:
        lock1.acquire()
        print('thead1:' + str(num))
        num += 1
        lock2.release()
        time.sleep(0.2)

def thread2():
    global num
    while num <= 100:
        lock2.acquire()
        print('thead2:' + str(num))
        num += 1
        lock3.release()
        time.sleep(0.2)

def thread3():
    global num
    while num <= 98:
        lock3.acquire()
        print('thead3:' + str(num))
        num += 1
        lock1.release()
        time.sleep(0.2)

if __name__ == "__main__":
    global num
    num = 0

    # 获取线程对象，并保存到线程序列中
    threads = []
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t3 = threading.Thread(target=thread3)
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    # 创建原锁
    lock1 = threading.Lock()
    lock2 = threading.Lock()
    lock3 = threading.Lock()
    # 获取除第一个线程外的其他原锁
    lock2.acquire()
    lock3.acquire()

    # 线程执行
    for thread in threads:
        thread.start()
    # 线程同步
    for thread in threads:
        thread.join()
    