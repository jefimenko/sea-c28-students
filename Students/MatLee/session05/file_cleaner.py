import io
import sys

try:
    filename = sys.argv[1]
except IndexError:
    print u'No filename given. Bye.'
    quit()

try:
    f = open(filename)
except IOError:
    f.close()

print f.closed   
f.close()
print f.closed