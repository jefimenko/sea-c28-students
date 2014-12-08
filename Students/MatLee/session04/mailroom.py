HISTORY = 'mailroom.txt'

def main():
    while True:
        print '(1) Send a Thank You.'
        print '(2) Create a Report.'
        print '(3) Exit program.'
        a = safe_input('Which would you like to do? ')
        if 'exit program' in a.lower():
            end()
        elif 'create a report' in a.lower():
            report()
        elif 'send a thank you' in a.lower():
            send()


def safe_input(display=""):
    try:
        return raw_input(display)
    except (EOFError, KeyboardInterrupt):
        return None


def send():
    print "thank you!"
    return


def report():
    print "report"
    return


def end():
    quit()

main()