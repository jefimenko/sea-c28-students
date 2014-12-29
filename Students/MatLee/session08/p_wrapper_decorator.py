def p_wrapper(func):
    """
    Takes a function that returns a string and wraps it in paragraph
    tags using string formatting.
    """
    def inner(*args):
        return u'<p> {0} </p>'.format(func(args))
    return inner

@p_wrapper
def return_a_string(text):
    # Check if the given input is a string.
    if not isinstance(text, str):
        raise TypeError
    # Make sure the input given is passed on in unicode.
    return unicode(text)
