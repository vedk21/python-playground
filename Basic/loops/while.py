# While loop

i = 0
while i < 10:
  print(i) # 1, 2, 3, ... so on
  i += 1

# else condition
j = 0
a = 11
while j < 10:
  print(j)
  if (j == a):
    break # breaks out of the loop
else:
  print('The loop didn\'t break')

# else is only executed if while loop completes without break

#pass
j = 0
while j < 10:
  pass # just a placeholder

# continue
j = 0
while j < 10:
  print(j)
  if (j > 5):
    continue # just continue the next iteration, neglect all the code after it
  print('never going to execute if j > 5')
