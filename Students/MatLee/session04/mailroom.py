def main():
    while True:
        print '(1) Send a Thank You.'
        print '(2) Create a Report.'
        print '(3) Exit program.'
        a = raw_input('Which would you like to do? ')
        if 'exit program' in a.lower():
            end()

def end():
    quit()

main()