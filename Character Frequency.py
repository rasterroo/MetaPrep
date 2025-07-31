def character_frequency(s, c):
  # Write your code here. NOTE: please do not use collections.counter() in the real interview.
  d = {}
  for char in s:
    d[char] = d.get(char,0)+1
    
  return d[c] if c in d else 0
