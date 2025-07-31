def return_missing_balanced_numbers(input):
  # Write your code here
  c = {}
  for i in input:
    c[i] = c.get(i,0)+1
  ret = {}
  target = max(c.values())
  for j in c:
    if c[j] < target:
      ret[j] = target-c[j]  
  return ret
