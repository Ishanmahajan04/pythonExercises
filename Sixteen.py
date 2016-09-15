def filter_long_words(lst, n):
  return [w for w in lst if len(w) > n]


print(filter_long_words(['asdas','sad','sd','asdasd','s'] , 2))