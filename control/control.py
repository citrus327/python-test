# https://automatetheboringstuff.com/2e/chapter2/

# name = 'Mary'
# password = 'aa'

# if name == 'Mary':
#   print('Hello, Mary')

#   if password == 'swordfish':
#     print('Access granted.')
#   elif password == 'xxx':
#     print('Wrong password.')
#   else:
#     print('xxx')

## while loop
# guess = input()
# name = 'Hao'
# while name != guess:
#   print('wrong guess, keep trying..')
#   guess = input()

# print('you guessed correctly')



## while loop with break
# name = 'Hao'
# while True:
#   if (name == input()):
#     break;
#   else:
#     print('wrong guess, keep trying..')

# print('you guessed correctly')



total = 0
for num in range(101):
  total = total + num
  
print(total)  