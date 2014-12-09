import io

HISTORY = u'mailroom.txt'
FORM_EMAIL = u'form_email.txt'

def main():
    data = read_info()
    
    while True:
        print
        print u'   Main Menu:'
        print u'(1) Send a Thank You.'
        print u'(2) Create a Report.'
        print u'(3) Exit program.'
        a = safe_input(u'   ')
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
    while True:
        print
        print u'   Thank You e-mail menu:'
        print u'(1) Enter full name of donor.'
        print u'(2) Enter \'list\' to show donor names.'
        print u'(3) Return to main menu.'
        b = safe_input(u'   ')
        if u'return to main menu' in b.lower():
            return
        elif u'list' in b.lower():
            print
            for name in data.iterkeys():
                print u' %s' % name
        else:
            # Won't worry about validating names for now
            # Create a new entry if non-existent
            amount = data.setdefault(b, [])
            amount.append(valid_d(data))
            email(b, amount[-1])
            return


def valid_d(data):
    while True:
        try:
            a = float(safe_input(u'   Input donation amount in dollars: '))
        except ValueError:
            print u'   Invalid input.'
            continue
        if a:
            return a


def email(name, donation):
    f = open(FORM_EMAIL)
    form = f.read()
    f.close()
    print
    print form % (name, donation)
    print
    return


def report(data):
    header = (u'|Name:', u'|Total donations:', 
              u'|# of donations:', u'|Average amount per donation:')
    print
    print u'%-25s%-15s%-16s%-29s'% header
    for donor, amounts, in data.iteritems():
        total = sum(amounts)
        donations = len(amounts)

        print u' %-25s%15.2f%16i%29.2f' % (
            donor, total, donations, total/donations
            )

    return


# Read previously saved information out of a file into a dictionary.
# Return an empty dictionary if there is no existing information.
def read_info():
    try:
        f = open(HISTORY)
    except IOError:
        f.close()
        return dict()
    data = eval(f.read())
    print data
    f.close()
    
    return data


def end(data):  
    save = open(HISTORY, 'w')
    save.write(str(data))
    save.flush()
    save.close()
    quit()


if __name__ == "__main__":
    main()