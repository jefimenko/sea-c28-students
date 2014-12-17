from rot13 import rot13

def test_shift():
    sample = u'abcdefghijklmnopqrstuvwxyz'

    assert rot13(sample) == sample.encode(u'rot13')
    assert rot13(sample.upper()) == sample.encode(u'rot13').upper()

# Test preservation of case, white space and non-alphabetical characters.
def test_preservation():
    sample = u'Hello?\n Well, I hope you have a nice day!@#$%^&*()_-=+/<>|{}[]01'

    assert rot13(sample) == sample.encode(u'rot13')