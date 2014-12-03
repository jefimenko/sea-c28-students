#!/user/bin/env python

def number():
    return 0
    
the_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
print the_list

the_list.append(unicode(raw_input(u"Input another fruit to add to this list: ").title()))
print the_list

print the_list[number()]

the_list = [u"Pomegranate"] + the_list
print the_list
the_list.insert(0, u"Pomelo")
print the_list

for fruit in the_list:
    if fruit[0] == u"P":
        print fruit,
else:
    print "\n"