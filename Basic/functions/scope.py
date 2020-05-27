# Python follow bottom to top (local to global) scope resolution technique

a = 5

def parent():
  def child():
    a = 10
    return a
  return child()

print(parent()) # 10
print(a) # 5

# Rule: 
# 1. Local scope
# 2. Parent local scope
# 3. Global scope
# 4. Built in functions

# access to global variables inside function

total = 0

def add_one():
  global total
  total += 1
  return total
add_one()
add_one()
print(add_one()) # 3

# don't use global unnecessary because it introduces the complexity and confusion

# access to parents local variables inside child function

def parent():
  a = 10
  def child():
    nonlocal a
    a = 20
    return a
  return child()

print(parent()) # 20
