import io
import sys


def save_file(copy, f):
    f.close()
    while True:
        a = raw_input(u'Would you like to overwrite existing file,\n'
                      u'or create a new file? ')
        if u'overwrite' in a.lower():
            writer(filename, copy)
            return
        elif u'create a new file' in a.lower():
            b = raw_input(u'Please name the new file: ')
            writer(b + '.txt', copy)
            return


def writer(name, copy):
    f = open(name, 'w')
    f.write('\n'.join(copy))
    f.close()
    return

    
try:
    filename = sys.argv[1]
except IndexError:
    print u'No filename given. Bye.'
    quit()

try:
    f = open(filename, 'r')
except IOError:
    f.close()
    print f.closed


copy = []
for line in f:
    copy.append(line.strip())

save_file(copy, f)

f.close()
