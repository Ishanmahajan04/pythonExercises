def find_longest_word(lst):
  longest = ""
  for w in lst:
    if len(w) > len(longest):
      longest = w
  return len(longest)