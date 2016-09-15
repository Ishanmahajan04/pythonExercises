import string.lowercase

rotate_by, key, alpha = 13, {}, lowercase

i = 0
while i < len(alpha):
    index = i + rotate_by

    if index > 25:
        index = index - 26

    key[alpha[i]] = alpha[index]
    i += 1

keyUpper = {}

for c in key:
    keyUpper[c.upper()] = key[c].upper()

key.update(keyUpper)


def caesar_cypher(str):
    result = ""
    for c in str:
        result += key[c] if c in key else c
    return result


# test
print (caesar_cypher('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))