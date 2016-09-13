def sum(lst):
  res = 0
  for i in lst:
    res += i
  return res

def multiply(lst):
  result = 1
  for i in lst:
    result *= i
  return result


result =  sum([2,4,45,3])
print(result)
result = multiply([32,5,6])
print(result)