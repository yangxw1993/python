import copy
a = [1, 2, 3]

b = a
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))