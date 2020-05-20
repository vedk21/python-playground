# Basic Data Types
int # integer numeric type
float # floating point number
bool # boolean
str # string (set of characters) (immutable)
list # collection of heterogeneous types (mutable)
tuple # collection of heterogeneous types (immutable)
set # collection of unique heterogeneous types (immutable)
dict # key value pair map
None # no-value type

print(type(3))
print(type(3.3))
print(type(True))
print(type('this is string'))
print(type([3, 'abcd', 4.5, False]))
print(type((3, 'abcd', 4.5, False)))
print(type({3, 'abcd', 4.5, False}))
print(type({'key': 3, 'value': 'abcd'}))
a = None
print(type(a))
