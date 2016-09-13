def max_in_list(lst):
  max = 0
  for n in lst:
    if n > max:
      max = n
  return max


print(max_in_list([3,56,34,5,56,34,34]))