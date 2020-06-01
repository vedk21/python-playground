# Functional programming seprates functions from data. Data is passed as an arguments to the functions parameters.

# Pure functions

def square(num):
  return num**2

print(square(10)) # 100
print(square(10)) # 100
print(square(5)) # 25
print(square(5)) # 25
print(square(5)) # 25

# Pure functions are functions with no side effects outside the function body and results into same output for same given input.
# These functions are very much used to write efficient codes with less number of bugs, also the result can be cached for given inputs.
