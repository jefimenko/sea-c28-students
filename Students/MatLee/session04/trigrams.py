from io import open
from random import choice

with open('sherlock_small.txt') as f:
    data = f.read()

# Split the text assuming only '--', white space, 
# or '\n' are used to delimit words. Punctuation is included in analysis.
data = data.split('--')

for chunk in data[:]:
    data.remove(chunk)
    data += chunk.split()

analysis = dict()

# Create auxiliary symbol that will hold two words
# previous to current entry in data.
# Print out the list for files two or less words in length.
try:
    temp = [data[0], data[1]]
    data[2]
except IndexError:
    print temp

# Sequences of three words are tabulated as tuples of leading two words as
# keys with a list holding all third words as the corresponding value.
# Grow analysis data, create new entries in the dictionary as needed.
for word in data[2:]:
    try:
        analysis[(temp[0], temp[1])].append(word)
    except KeyError:
        analysis[(temp[0], temp[1])] = [word]
    temp[0], temp[1] = temp[1], temp[0]
    temp[1] = word

"""
for iden, thing in analysis.iteritems():
    if len(thing) > 1:
        print iden, thing
"""

temp = choice(analysis.keys())
temp = [temp[0], temp[1]]
out = temp[:]

while analysis.has_key((temp[0], temp[1])):
    out.append(choice(analysis[(temp[0], temp[1])]))
    temp[0], temp[1] = temp[1], out[-1]

out[0] = out[0].title()
print ' '.join(out)