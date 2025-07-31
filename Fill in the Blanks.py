def fill_in_the_blanks(input_lst):
  # Write your code here
  most_recent = None
  ret = []
  for i in input_lst:
    if i is None:
      ret.append(most_recent)
    else:
      ret.append(i)
      most_recent = i
  return ret
