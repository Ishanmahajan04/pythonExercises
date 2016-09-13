def is_member(ele, lst):
  for e in lst:
    if ele == e:
      return True
  return False


print(is_member(3,[3,"a",1,"i"]))