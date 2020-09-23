import time


class Classmate(object):

    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """"如果想对一个对象可迭代，可以使用for，必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            raise StopIteration


classmate = Classmate()
classmate.add('Chris')
classmate.add('Andy')

for item in classmate:
    print(item)
    time.sleep(1)