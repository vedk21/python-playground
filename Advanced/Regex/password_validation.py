# Password validation
# It should contain letters, numbers, @#$% allowed, should be at least 8 characters and end with number

import re

pattern = re.compile(r"([A-Za-z0-9$%#@]{7,}[0-9])")
password = 'secret123@99'

matched = pattern.fullmatch(password)
if matched:
  print('You are successfully logged in!')
else:
  print('Sorry, wrong password')
