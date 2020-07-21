def remove(x):
  x.pop(0)
  x.pop(4-1)
  x.pop(5-2)
  return x
  
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove(color))