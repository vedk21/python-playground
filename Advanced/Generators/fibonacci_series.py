# Fibonacci series using generators

def fib(num):
  first = 0
  second = 1
  for _ in range(num):
    yield first
    temp = first
    first = second
    second = temp + second

for i in fib(15):
  print(i)
