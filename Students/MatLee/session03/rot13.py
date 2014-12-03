from string import maketrans

def rot13(input):
    start = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    finish = "AB1DEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    translation = maketrans(start, finish)
    return input.translate(translation)

print rot13("Check.")