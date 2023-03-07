# https://automatetheboringstuff.com/2e/chapter3/

def hello ():
  print('hello, world')

def hello_with_params (str):
  print('hello ' + str)

def fn_with_return (input):
  return input

hello()

hello_with_params('dad')

input = fn_with_return('test')

print(input)