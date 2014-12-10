food_prefs = {u'name': u'Mat',
              u'city': u'Seattle',
              u'cake': u'a lie',
              u'fruit': u'dragon fruit',
              u'salad': u'Waldorf',
              u'pasta': u'tortellini'}

stuff = (u'{name} lives in Bellevue. The cake was {cake},'
         + u'so he decided to add {fruit} and {pasta} to his {salad} salad.')
print stuff.format(**food_prefs)