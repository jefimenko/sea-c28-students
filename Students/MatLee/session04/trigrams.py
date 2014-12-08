from io import open
import random

#FILE_NAME = 'pg28659.txt'
FILE_NAME = 'sherlock_small.txt'

with open(FILE_NAME) as f:
    data = f.read()

# Split the text assuming only white space is used to delimit words.
# Punctuation is included in analysis and two consecutive \n characters
# are interpreted as paragraph separations.

data = data.split('\n')

for chunk in data[:]:
    data.remove(chunk)
    data += chunk.split()
    data.append('\n')


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


temp = random.choice(analysis.keys())
temp = [temp[0], temp[1]]
print temp[0].title(),
print temp[1],

while analysis.has_key((temp[0], temp[1])):
    n = random.choice(analysis[(temp[0], temp[1])]) # doesn't perform well for large files...
    print n,
    temp[0], temp[1] = temp[1], n

"""
out[0] = out[0].title()
for word in out:
    print word,
"""