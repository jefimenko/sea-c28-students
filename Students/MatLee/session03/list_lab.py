#!/user/bin/env python

def number():
    valid = range(1, len(the_list)+1)

    while True:
        
        temp = raw_input("Please input a number between 1 and %i." % len(the_list))
        temp = int(temp)

        if temp in valid:
            return temp - 1
        else:
            print "Invalid input."
            continue
    
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