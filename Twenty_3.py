
suffixes = ('o', 'ch', 's', 'sh', 'x', 'z')
def make_3sg_form(verb):
  if verb.endswith('y'):
    return verb[:-1]+'ies'
  elif verb.endswith(suffixes):
    return verb+'es'
  else:
    return verb+'s'

print (make_3sg_form('ishan'))