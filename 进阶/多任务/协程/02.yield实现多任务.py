import time
import random


def task_1():
    while True:
        random_num = random.randint(0, 100)
        print('****task1>>', random_num)
        time.sleep(1)
        yield


def task_2():
    while True:
        random_num = random.randint(0, 100)
        print('****task2>>', random_num)
        time.sleep(1)
        yield


def main():

    t1 = task_1()
    t2 = task_2()

    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()