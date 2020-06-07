# Regular expression pattern

import re

pattern = re.compile('here')
pattern2 = re.compile('Hi there')
str = 'Hi there! You are welcome here.'

match_obj = pattern.search(str)
print(match_obj.group()) # here
print(match_obj.span()) # (4, 8)

all_matched_str = pattern.findall(str)
print(all_matched_str) # ['here', 'here']

full_matched_str = pattern2.fullmatch(str)
print(full_matched_str) # None

matched_str = pattern2.match(str)
print(matched_str.span()) # (0, 8)
