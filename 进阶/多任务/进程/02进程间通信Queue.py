import multiprocessing


def download_data(q):
    """"下载数据"""
    data_list = [11, 22, 33, 44, 55]
    for item in data_list:
        q.put(item)
    print('数据已放到队列当中')


def analysis_data(q):
    """"handle data"""
    analysis_data_list = list()
    while True:
        data = q.get()
        analysis_data_list.append(data)
        if q.empty():
            break
    print('已经处理的数据', analysis_data_list)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_data, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()