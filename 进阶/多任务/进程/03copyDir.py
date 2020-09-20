import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    """"完成文件的复制"""
    old_f = open(f'{old_folder_name}/{file_name}', 'rb')
    content = old_f.read()
    old_f.close()

    new_f = open(f'{new_folder_name}/{file_name}', 'wb')
    new_f.write(content)
    new_f.close()


def main():
    # get need copy dir name 获取需要copy 的文件夹名字
    old_folder_name = input('Please need copy dir name：')

    # 2.creat new dir
    new_folder_name = old_folder_name + '[复件]'
    os.mkdir(new_folder_name)

    # 3. get dir all file name => listdir()
    file_names = os.listdir(old_folder_name)

    # 4.create processing pool
    pool = multiprocessing.Pool(5)

    # 5.to pool add copy file plan
    for file_name in file_names:
        pool.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
    pool.close()
    pool.join()
    # copy old file to new dir


    pass


if __name__ == '__main__':
    main()