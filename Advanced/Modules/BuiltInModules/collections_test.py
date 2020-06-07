# Collections package

from collections import defaultdict, OrderedDict, Counter

# count number of occurrences of items in an iterable
print(Counter('How are you')) # this is case-sensitive
# Counter({'o': 2, ' ': 2, 'H': 1, 'w': 1, 'a': 1, 'r': 1, 'e': 1, 'y': 1, 'u': 1})

# default dictionary returns custom value instead of error if key doesn't exists in dictionary is accessed
d = defaultdict(lambda: 'key doesn\'t exists', {'a': 1, 'b': 2})
print(d['a']) # 1
print(d['c']) # key doesn't exists

# Ordered dictionaries will be used to maintain order in dictionary
d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}
print(d1 == d2) # True

d3 = OrderedDict()
d3['a'] = 1
d3['b'] = 2

d4 = OrderedDict()
d4['b'] = 2
d4['a'] = 1

print(d3 == d4) # False, because the order is different

# Recently, the Python has made Dictionaries ordered by default! So unless you need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!