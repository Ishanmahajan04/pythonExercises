def find_longest_word(words):
  return max(map(len, words))

print (find_longest_word(['This', 'is', 'unacceptable']))