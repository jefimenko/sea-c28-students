from io import open

with open('sherlock_small.txt') as f:
    out = f.read()

# Split the text assuming only '--', white space, 
# or '\n' are used to delimit words. Punctuation is included in analysis.
out = out.split('--')

for chunk in out[:]:
    out.remove(chunk)
    out += chunk.split()

analysis = dict()

# Create auxiliary symbol that will hold two words
# previous to current entry in data.
# Print out the list for files two or less words in length.
try:
    temp = [out[0], out[1]]
    out[2]
except IndexError:
    print temp

for word in out[2:]:
    analysis.setdefault((temp[0], temp[1]), word)
    temp[0], temp[1] = temp[1], temp[0]
    print temp
    temp[1] = word
    print temp

print analysis