# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(myCat)

# # comparision
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print('two dicts with same items are identical', eggs == ham)

# convert to list basically === list(dict.keys())
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# print(list(eggs)) # ['name', 'species', 'age']
# ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
# print(list(ham)) # ['species', 'age', 'name']
# print(list(ham.keys()) == list(ham))

# keys will remember inserted order
# spam = {}
# spam['first key'] = 'value'
# spam['second key'] = 'value'
# spam['third key'] = 'value'
# list(spam)

# setdefault
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam.setdefault('color', 'white')
print(spam['color']) # white does not over write black