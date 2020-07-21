def one_common(x,y):
  if len(set(x).intersection(set(y))) > 0:
    return True
  else:
    return False
    
    
print(one_common([1,2,3,4,5], [5,6,7,8,9]))
print(one_common([1,2,3,4,5], [6,7,8,9]))