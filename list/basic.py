# list = [1, 2, 3, 4, 5]

# print(list[1])

# # negative indices
# print(list[-1])

# # slice
# print(list[0:2])
# print(list[0:10])
# print(list[1:4])
# print(list[1:])
# print(list[:5])
# print(list[:])

## length
# list = [1, 2, 3, 4, 5]
# print(len(list))

# concat
# print([1, 2] + [2, 3])

## equal
# list2 = [1, 2, 3]
# span = list2 + []
# print(list2, span, sep="\n")
# print(list2 == span)
# print(list2 is span)

# # include & not include
# print(2 in [1, 2] + [2, 3])
# print(4 not in [1, 2] + [2, 3])

# # assignment
# cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
# a, b, c = cat
# print(size, color, disposition, sep=" ")
# print(a, b, c, sep=" ")

## Loop
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
  print('Index', str(i), 'in supplies is:', supplies[i], sep=" ")

for i, item in enumerate(supplies):
  print('index is', i, 'item is', item, sep=" ")

print(supplies.index('pens'))
print(supplies.append('123'), supplies)
print(supplies.insert(1, '123'), supplies)
