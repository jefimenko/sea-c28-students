def main():
    while True:
        print '(1) Send a Thank You.'
        print '(2) Create a Report.'
        print '(3) Exit program.'
        a = safe_input('Which would you like to do? ')
        if 'exit program' in a.lower():
            end()

def safe_input(display=""):
    try:
        return raw_input(display)
    except (EOFError, KeyboardInterrupt):
        return None

def end():
    quit()

main()