import time
import threading

num = 10000000
count = 10000000
# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def tes1():
    global num
    # 没有上锁就上锁，上锁的话就一直等待
    mutex.acquire()
    for i in range(count):
        num += 1
    print(f'test 1 num is {num}')
    mutex.release()


def tes2():
    global num
    mutex.acquire()
    for i in range(count):
        num += 1
    print(f'test 2 num is {num}')
    mutex.release()

def main():
    t1 = threading.Thread(target=tes1)
    t2 = threading.Thread(target=tes2)

    t1.start()
    t2.start()
    time.sleep(5)
    print(f'global num is {num}')


if __name__ == '__main__':
    main()
