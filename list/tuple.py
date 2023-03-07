# https://automatetheboringstuff.com/2e/chapter4/
# Tuples cannot have their values modified, appended, or removed

eggs = ('hello', 42, 0.5)
print(eggs[0])

# <class 'str'> <class 'tuple'>
print(type(('hello')))
print(type(('hello', )))


# type convertion
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))