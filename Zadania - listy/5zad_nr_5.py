def count(x):
  sum = 0
  for n in x:
    if len(n)>=2 and (n[0]==n[-1]):
      sum += 1
  return sum
      
lis = ['abc', 'xyz', 'aba', '1221']

print(count(lis))