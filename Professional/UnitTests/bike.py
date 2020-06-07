# Bike code file

def drive(action):
  try:
    action = action.upper()
  except AttributeError as err:
    return err

  if action == 'DRIVE_FAST':
    return 130
  elif action == 'DRIVE_SLOW':
    return 15
  elif action == 'EMERGENCY':
    return 45
  else:
    return 'Invalid Action'
