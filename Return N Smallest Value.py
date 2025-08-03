def return_smallest_key(inputDict, n):
  # Write your code here
  if n==0 or n>len(inputDict): return None
  sd = sorted(inputDict.items(), key=lambda x: (x[1], x[0]))
  
  return sd[n-1][0]
