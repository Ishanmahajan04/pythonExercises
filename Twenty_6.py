def max_in_list(lst):
  return reduce(lambda x, y: x if x > y else y, lst)


print (max_in_list([1,2,3,4,5,6,10,3]))