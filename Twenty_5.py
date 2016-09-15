
vowels = 'aeiou'
def make_ing_form(verb):
  if verb.endswith('ie'):
    return verb[:-2]+'ying'
  elif verb.endswith('e'):
    return verb[:-1]+'ing'
  elif verb[-3] not in vowels:
    if verb[-2] in vowels:
      if verb[-1] not in vowels:
        return verb+verb[-1]+'ing'
  else:
    return verb+'ing'


  print(make_ing_form('rasde'))