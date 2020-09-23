import time


class Classmate(object):

    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return ClassIterator(self)


class ClassIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            result = self.obj.names[self.current_num]
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