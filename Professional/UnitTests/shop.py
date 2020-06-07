# shop code file

def add_to_cart(item, li):
  try:
    if len(item) and item[0]:
      li.append({'id': int(item[0]) + 10, 'item': item[1]})
      return li
    else:
      return 'Invalid item'
  except ValueError as err:
    return err
