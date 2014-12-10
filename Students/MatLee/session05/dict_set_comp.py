food_prefs = {u'name': u'Mat',
              u'city': u'Seattle',
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
print 'd'
print d

j = {x: hex(x)[2:] for x in range(16)}
print 'j'
print j