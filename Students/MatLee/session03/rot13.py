from string import maketrans

def rot13(input):
    """Return a translation of a string, input.
    A cyclical shift of 13 alphabetical places for letters only, 
    preserving white space, case, and punctuation."""
    input = str(input)
    start = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    finish = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    translation = maketrans(start, finish)
    return unicode(input.translate(translation))


if __name__ == "__main__":
    #Verify that the returned string is in unicode.
    print "%r" % rot13("Check.")
    #Verify that the function performs as desired.
    assert (rot13(u"ABCDEFGHIJKLMNOPQRSTUVWXYZ. abcdefghijklmnopqrstuvwxyz123")
            == u"NOPQRSTUVWXYZABCDEFGHIJKLM. nopqrstuvwxyzabcdefghijklm123")
