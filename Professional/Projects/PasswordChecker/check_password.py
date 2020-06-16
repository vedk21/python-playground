# Check password

import requests
import hashlib
import sys

def request_api(password_hash):
  url = f'https://api.pwnedpasswords.com/range/{password_hash}' # first 5 characters of password hash
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error in API {res.status_code}, please check the request')
  return res

def get_pwned_stats(pwnd_hash_list, hash_to_check):
  # convert pwnd_hash_list into tuple with (hash, count)
  hash_stats = (stat.split(':') for stat in pwnd_hash_list.text.splitlines())
  # check the hash with our hashed_password
  for h, count in hash_stats:
    if h == hash_to_check:
      return count
  return 0

def check_pwned_api(password):
  sha1_password = hashlib.sha1(password.encode('utf8')).hexdigest().upper()
  first_5_char, remaining_char = sha1_password[:5], sha1_password[5:]
  result = request_api(first_5_char)
  return get_pwned_stats(result, remaining_char)

def main(args):
  if args and len(args):
    for password in args:
      pwned_count = check_pwned_api(password)
      if pwned_count:
        print(f'{password} was found {pwned_count} times. You should consider changing your password')
      else:
        print(f'{password} was not found. You are good to go with this password')
  else:
    print('Please enter passwords as command line arguments')

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
