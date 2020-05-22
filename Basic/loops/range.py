# Range object
# Range is a object which is iterable and return a sequence of intergers

print(range(0, 100)) # print a range object range(0, 100)

# we can use range in for loops
for item in range(0, 100):
  print(item) # prints from 0 -> 99

# when we don't want to use the local variable
for _ in range(0, 100):
  print('send email!!!')

# stepping
for item in range(0, 20, 2):
  print(item) # all even numbers will be printed

#reverse order iteration
for item in range(10, 0, -1):
  print(item)

# create list using range
print(list(range(0, 5))) # [0, 1, 2, 3, 4]
