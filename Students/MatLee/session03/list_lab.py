#!/user/bin/env python

def number():
    valid = range(1, len(the_list)+1)

    while True:
        
        temp = raw_input(u"Please input a number between 1 and %i." % len(the_list))
        temp = int(temp)

        if temp in valid:
            return temp - 1
        else:
            print u"Invalid input."
            continue
"""
def like():
    for fruit in the_list:
        print "Do you like %ss?" % fruit
        if True:
            continue
        elif False:
            #remove
    return None
"""

#series 1
the_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
print the_list

the_list.append(unicode(raw_input(
                u"Input another fruit to add to this list: "
                ).title()))
print the_list

print the_list[number()]

the_list = [u"Pomegranates"] + the_list
print the_list
the_list.insert(0, u"Pomelo")
print the_list

for fruit in the_list:
    if fruit[0] == u"P":
        print fruit,
else:
    print "\n"

#series 2
print the_list
del the_list[-1]
print the_list

flag = True
while flag:
    temp = raw_input(u"Select a fruit from the list to delete. ")
    temp = unicode(temp.title())
    if temp in the_list:
        flag = False
        the_list.remove(temp)
    else:
        print u"Invalid input."
        continue
print the_list
##try with a doubled list, deleted all instances


#series 3
for fruit in the_list[:]:
    invalid = True
    while invalid:
        temp = raw_input(u"Do you like %s? " % fruit.lower())
        temp = unicode(temp)
        if temp.lower() == u"yes":
            invalid = False
        elif temp.lower() == u"no":
            invalid = False
            the_list.remove(fruit.title())
        else:
            print u"Please answer 'yes' or 'no.'"
            continue


#series 4
copy = the_list[:]
print copy
for x in range(len(copy)):
    copy[x] = copy[x][::-1]
del the_list[-1]
print the_list
print copy