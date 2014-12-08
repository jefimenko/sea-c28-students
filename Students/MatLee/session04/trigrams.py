from io import open

with open('sherlock_small.txt') as f:
    out = f.read()

print f.closed
print out
out = out.split('--')
print out


for chunk in out[:]:
    out.remove(chunk)
    out += chunk.split()

print repr(out)

#for word in out:
#    print repr(word)

