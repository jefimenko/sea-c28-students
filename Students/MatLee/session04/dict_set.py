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

b = range(16)
c = []
for num in b:
    c.append(hex(num)[2:])
dec_hex = dict(zip(b, c))
print dec_hex


things = stuff.items()
for b in range(len(things)):  
    things[b] = (things[b][0], things[b][1].count('a'))

stuff_prime = dict(things)
print stuff
print stuff_prime