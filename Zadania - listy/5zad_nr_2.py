def multiply_numbers(x):
  sum = 1
  for n in x:
    sum *= n
  return sum
    
    
li = [2,2,3]

print(multiply_numbers(li))