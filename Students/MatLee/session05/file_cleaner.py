import io
import sys


def save_file(copy, f):
    f.close()
    while True:
        a = raw_input(u'Would you like to overwrite current file,\n'
                      u'or create a new file/overwrite a different file? ')
        if u'overwrite current file' in a.lower():
            writer(filename, copy)
            return
        elif (u'create a new file' in a.lower() 
              or u'overwrite a different file' in a.lower()):
            b = raw_input(u'Please name the new/overwrite file: ')
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
    print u'File not found. Bye.'
    quit()

# First version.
# copy = []
# for line in f:
    # copy.append(line)
# copy = map(str.strip, copy)

# Second version using list comprehension.
copy = [line in f]
copy = map(str.strip, copy)

save_file(copy, f)

f.close()
