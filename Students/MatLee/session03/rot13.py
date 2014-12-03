from string import maketrans

def rot13(input):
    """Return a translation of a string, input.
    A cyclical shift of 13 alphabetical places for letters only, 
    preserving white space, case, and punctuation."""
    start = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    finish = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    translation = maketrans(start, finish)
    return input.translate(translation)

if __name__ == "__main__":
    assert (rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ. abcdefghijklmnopqrstuvwxyz")
            == "NOPQRSTUVWXYZABCDEFGHIJKLM. nopqrstuvwxyzabcdefghijklm")
