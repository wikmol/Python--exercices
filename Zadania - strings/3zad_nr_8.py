def the_longest(words):
  lengths = [len(x) for x in words]
  return max(lengths)
  
x = ['abc','wiktor','dracula','z']

print(the_longest(x))