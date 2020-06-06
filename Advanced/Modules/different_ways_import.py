# There are various ways to import modules

import utility
from Packages.shopping_cart.shopping_cart import buy, max as maxString

# If there is a name conflicts between functions of packages, then its better to import the complete package or create alias of that function

print(buy('oranges')) # ['oranges']
print(utility.sum(6, 3)) # 9
print(max([1, 2, 3])) # 3
print(maxString('hey', 'hi')) # 'hey'
