def concatenate(list):
  x = ""
  for n in list:
    x += str(n)
  return x
  
  
list = [1,2,3]

print(concatenate(list))