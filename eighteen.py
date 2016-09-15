import string

alpha = string.ascii_lowercase

def is_pangram(str):
  found = []
  for c in str.lower():
    if c in alpha and c not in found:
      found.append(c)
  if len(found) == len(alpha):
    return True
  else:
    return False


print (is_pangram("The quick brown fox jumps over the lazy dog"))