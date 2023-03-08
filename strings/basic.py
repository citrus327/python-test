name = 'Al'
age = 4000
print('My name is %s. I am %s years old.' % (name, age))

"""this is a comment?....jesus
Reprehenderit amet ipsum mollit ea aliquip do id in ipsum est aliquip.
"""

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')


print(', '.join(['cats', 'rats', 'bats']))
print('My name is Simon'.split()) # default using whitespace as a seperator
print('My name is Simon'.split(' '))

# string partition, only partition target on the first occourance
print('Hello, world!'.partition('o'))
print('Hello, world!'.partition('xx'))

before, sep, after = 'Hello, world!'.partition(' ')
print({'before': before, 'sep': sep, 'after': after})

# right and left justify, total 20 letters, fill asterisk on left right and both sides
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '*'))
print('Hello'.center(20, '*'))

# strip
print('    Hello, World    '.strip(), end="END!\n")
print('    Hello, World    '.lstrip(), end="END!\n")
print('    Hello, World    '.rstrip(), end="END!\n")




