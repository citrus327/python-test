def append(someParameter):
    someParameter.append('Hello')

list = [1, 2, 3]
list_id = id(list)
append(list)
print(list)

import copy
print('id:', id(list), sep=" ")
print('id:', id(copy.copy(list)), sep=" ")
append(list)
print('after append, id does not change.', list_id == id(list), sep=" ")
print('two copies but with same id', id(copy.copy(list)) == id(copy.copy(list)), sep=" ")


