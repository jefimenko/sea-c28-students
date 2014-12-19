food_prefs = {u'name': u'Mat',
              u'city': u'SeAttle',
              u'cake': u'a lie',
              u'fruit': u'dragon fruit',
              u'salad': u'Waldorf',
              u'pasta': u'tortellini'}

stuff = (u'{name} lives in Bellevue. The cake was {cake},'
         + u'so he decided to add {fruit} and {pasta} to his {salad} salad.')
print stuff.format(**food_prefs)

# Create dictionary of numbers, as keys, and hexadecimal equivalents.
# Hex values are represented as strings, omitting leading characters.
d = dict([(x, hex(x)[2:]) for x in range(16)])

j = {x: hex(x)[2:] for x in range(16)}

# Using dictionary comprehension, modify values in food_prefs to the number of
# 'a's in the value.
food_prefs = {thing: specific.count('a') + specific.count('A') for thing, specific in food_prefs.iteritems()}


s2 = {x for x in range(21) if not (x % 2)}
s3 = {x for x in range(21) if not (x % 3)}
s4 = {x for x in range(21) if not (x % 4)}


# Updated:
s_all = []
for item in range(2, 5):
    s_all.append({x for x in range(21) if not (x % item)})
print s_all

d_all = [{x for x in range(21) if not (x % item)} for item in range(2,5)]
print d_all
