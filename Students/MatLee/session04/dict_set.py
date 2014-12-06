stuff = {"name": "Chris", 
         "city": "Seattle", 
         "cake": "Chocolate"}

print stuff
stuff.pop("cake")
print stuff
stuff.setdefault("fruit", "Mango")
print stuff.keys()
a = stuff.values()
print a
print "cake" in stuff
print "Mango" in a

c = []
for num in range(16):
    c.append(hex(num)[2:])
dec_hex = dict(zip(range(16), c))
print dec_hex


things = stuff.items()
for b in range(len(things)):  
    things[b] = (things[b][0], things[b][1].count('a'))

stuff_a = dict(things)
print stuff
print stuff_a


s2 = set()
s3 = set()
s4 = set()

for num in range(1,21):
    if num % 2 is 0:
        s2.add(num)
    if num % 3 is 0:
        s3.add(num)
    if num % 4 is 0:
        s4.add(num)
else:
    print s2
    print s3
    print s4

print s3.issubset(s2)
print s4.issubset(s2)


letters = set('Python'[:])
letters.add('i')
print letters

frozen = frozenset('marathon'[:])
print frozen

print letters.union(frozen)
print letters.intersection(frozen)