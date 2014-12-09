import io

HISTORY = u'mailroom.txt'
FORM_EMAIL = u'form_email.txt'

def main():
    data = read_info()
    print data
    
    while True:
        print u'   Main Menu:'
        print u'(1) Send a Thank You.'
        print u'(2) Create a Report.'
        print u'(3) Exit program.'
        a = safe_input(u'   Which would you like to do? ')
        if u'exit program' in a.lower():
            end(data)
        elif u'create a report' in a.lower():
            report(data)
        elif u'send a thank you' in a.lower():
            send(data)
        else:
            print u'   Invalid input, please choose an entry from the menu.'


def safe_input(display=u''):
    try:
        return raw_input(display)
    except (EOFError, KeyboardInterrupt):
        return None


def send(data):
    print "thank you!"
    return


def report(data):
    header = (u'|Name:', u'|Total donations:', 
              u'|# of donations:', u'|Average amount per donation:')
    print u'%-25s%-17s%-16s%-12s'% header
    for donor, amounts, in data.iteritems():
        total = sum(amounts)
        donations = len(amounts)

        print u' %-26s %13.2f %15i %28.2f' % (
            donor, total, donations, total/donations
            )

    return


# Read previously saved information out of a file into a dictionary.
# Return an empty dictionary if there is no existing information.
def read_info():
    data = dict()
    try:
        f = open(HISTORY)
    except IOError:
        f.close()
        return data
    
    for line in f.readlines():
        temp = line.strip()
        temp = temp.split(', ')
        for x in range(1, len(temp)):
            temp[x] = float(temp[x])
        data[temp[0]] = temp[1:]
    
    f.close()
    return data


def save_info(data):
    print 'save to HISTORY! (not, actually)'
    return


def end(data):
    save_info(data)
    quit()


main()