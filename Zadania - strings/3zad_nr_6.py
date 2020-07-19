def add_ing(x):
  if len(x)<3:
    return 3
  else:
    if x[-3:] =="ing":
      return x + "ly"
    else:
      return x + "ing"
      
print(add_ing("swiming"))