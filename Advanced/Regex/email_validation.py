# Email validation using regex

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = 'ved21@mail.com'

matched = pattern.fullmatch(email)
if matched:
  print('You are successfully logged in!')
else:
  print('Sorry, wrong email id')
