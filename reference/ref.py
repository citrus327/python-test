# def append(someParameter):
#     someParameter.append('Hello')

# list = [1, 2, 3]
# list_id = id(list)
# append(list)
# print(list)

# import copy
# print('id:', id(list), sep=" ")
# print('id:', id(copy.copy(list)), sep=" ")
# append(list)
# print('after append, id does not change.', list_id == id(list), sep=" ")
## python interning
# print('two copies but with same id', id(copy.copy(list)) == id(copy.copy(list)), sep=" ")

import copy
list = [1, 2, 3]
t = copy.copy(list)
p = copy.copy(list)
t.append(1)
p.append(2)

print(t == p)
print(id(t) == id(p))
## python interning
print(id(copy.copy(t)) == id(copy.copy(p)))


