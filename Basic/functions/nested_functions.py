# Nessted functions

def show_user_total_score(name, scores = []):
  def get_total_score(total_scores = []):
    return sum(total_scores)
  return f'Hey {name}, your total score is {get_total_score(scores)}'

message = show_user_total_score('Mark', [10, 12, 40])
print(message) # 'Hey Mark, your total score is 62'

# nested function only exist inside parent function, they can not be invoked from outside the parent function
