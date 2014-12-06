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