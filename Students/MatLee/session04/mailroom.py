import io

HISTORY = u'mailroom.txt'
FORM_EMAIL = u'form_email.txt'

MAIN_MENU = ( u'\n   Main Menu:'
             +u'\n(1) Send a Thank You.'
             +u'\n(2) Create a Report'
             +u'\n(3) Exit program.' )
THANK_YOU_MENU = ( u'\n   Thank You e-mail menu:'
                  +u'\n(1) Enter full name of donor.'
                  +u'\n(2) Enter \'list\' to show donor names'
                  +u'\n(3) Return to main menu.' )
DONATION_MENU = ( u'\n(1) Input donation amount in dollars.'
                 +u'\n(2) Return to main menu. *short menu input disallowed' )


def main():
    """
    Display main menu and direct user to available courses of action.
    """
    data = read_info()
    print data
    while True:
        print MAIN_MENU
        a = raw_input(u'   ')
        if u'exit program' in a.lower() or u'3' == a:
            end(data)
        elif u'create a report' in a.lower() or u'2' == a:
            report(data)
        elif u'send a thank you' in a.lower() or u'1' == a:
            send(data)
        else:
            print u'   Invalid input, please choose an entry from the menu.'

def send(data):
    """
    Send a thank you e-mail to a donor and log the amount donated.
    """
    while True:
        print THANK_YOU_MENU
        b = raw_input(u'   ')

        if u'return to main menu' in b.lower() or u'3' == b:
            return
        elif u'list' in b.lower() or u'2' == b:
            print
            for name in data.iterkeys():
                print u' %s' % name
        else:
            # Prevent entries of only numbers from being passed as a name.
            # Will not filter prevent a mix of numbers and other characters
            # from being taken as a name.
            try:
                b = int(b)
                print u'   Please enter a name or valid menu option.'
                continue
            except ValueError:
                pass

            amount = valid_d(data)
            if not amount:
                return
            # Sets all names to title case.
            entry = data.setdefault(b.title(), [])
            entry.append(amount)
            email(b, entry[-1])
            return

def valid_d(data):
    """
    Prompt user and take input until a positive number is given.
    """
    while True:
        print DONATION_MENU
        a = raw_input(u'  $')
        # Disallow shorter input of option number, to allow option of
        # accepting a donation equal to 2
        if 'return to main menu' in a.lower():
            return

        try:
            a = float(a)
        except ValueError:
            print u'   Invalid input.'
            continue

        if a and (a > 0):
            return a
        else:
            print u'   Please input a positive amount.'

def email(name, donation):
    """
    Read a form email from a text file.
    """
    try:
        f = open(FORM_EMAIL)
        form = f.read()
    except IOError:
        raise IOError
    finally:
        f.close()
    print
    print form % (name, donation)
    print
    return

def report(data):
    """
    Print a report of donors and information about donation history.
    """
    header = (u'|Name:', u'|Total donations:', 
              u'|# of donations:', u'|Average amount per donation:')

    print u'\n%-20s%-15s%-16s%-29s'% header
    info = data.items()
    info = sorted(info, key=lambda c: sum(c[1]), reverse=True)

    for donor, amounts, in info:
        total = sum(amounts)
        donations = len(amounts)

        print u' %-20s%15.2f%16i%29.2f' % (
            donor, total, donations, total/donations
            )

    return

def read_info():
    """
    Open and read a file containing donation history.
    If the file fails to evaluate as a dictionary or is improperly formatted,
    a new history is created and the existing file is overwritten upon exiting
    the program.
    """
    try:
        f = open(HISTORY)
        data = dict( eval(f.read()) )
    except IOError:
        raise IOError
    except (AttributeError, NameError, SyntaxError, ValueError):
        print u'   Improperly formatted donor history.'
        data = dict()
    finally:
        f.close()

    return data

def end(data):
    """
    Save donor information to a file and exit the program.
    """
    try:
        save = open(HISTORY, 'w')
        save.write(str(data))
        save.flush()
    except IOError:
        raise IOError
    finally:
        save.close()
    quit()


if __name__ == "__main__":
    main()
