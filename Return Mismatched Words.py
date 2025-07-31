def return_mismatched_words(str1, str2):
  s1, s2 = str1.split(), str2.split()
  s1, s2 = set(s1), set(s2)
  output = []
  
  for s in s1:
    if s not in s2:
      output.append(s)
      
  for s in s2:
    if s not in s1:
      output.append(s)
      
  return output
