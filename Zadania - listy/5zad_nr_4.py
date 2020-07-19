def min_number(x):
  min = x[0]
  for n in x:
    if n < min:
      min = n
  return min
  
lis = [3,2,1,4]

print(min_number(lis))