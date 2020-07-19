def string_change(x):
  if len(x) < 2:
    return  ""
  else:
    return x[0:2] + x[-2:]
    
    
print(string_change("abcdef"))
print(string_change("a"))