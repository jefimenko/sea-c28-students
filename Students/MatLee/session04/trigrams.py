from io import open
import random

#FILE_NAME = 'pg28659.txt'
FILE_NAME = 'sherlock_small.txt'
#FILE_NAME = 'sherlock.txt'

def read_data(file_name):
    """
    Open a file and separate into 'chunks' delimited by '\n' characters.
    Return a list of the 'chunks'.
    """
    with open(file_name) as f:
        data = f.read()
    # Split the text assuming only white space is used to delimit words.
    # Punctuation is included in analysis and two consecutive \n characters
    # are interpreted as paragraph separations.
    data = data.split('\n')
    return data

def chunker(data):
    """
    Break 'chunks' into individual words, and reinsert '\n' characters
    after each 'chunk'.
    """
    for chunk in data[:]:
        data.remove(chunk)
        data += chunk.split()
        data.append('\n')
    return data

def analyze(data):
    """
    Create a dictionary containing analysis of a text broken up into words.
    """
    # Create auxiliary symbol that will hold two words
    # previous to current entry in data.
    # Print out the list for files two or less words in length.
    try:
        temp = [data[0], data[1]]
        data[2]
    except IndexError:
        print temp

    analysis = dict()
    # Sequences of three words are tabulated as tuples of leading two words as
    # keys with a list holding all third words as the corresponding value.
    # Grow analysis data, create new entries in the dictionary as needed.
    for word in data[2:]:
        try:
            analysis[(temp[0], temp[1])].append(word)
        except KeyError:
            analysis[(temp[0], temp[1])] = [word]
        temp[0], temp[1] = temp[1], temp[0]
        temp[1] = word
    return analysis

def out_write(analysis):
    """
    Produce output based on the results of analyze().
    """
    temp = random.choice(analysis.keys())
    temp = [temp[0], temp[1]]
    print temp[0].title(),
    print temp[1],

    while analysis.has_key((temp[0], temp[1])):
        n = random.choice(analysis[(temp[0], temp[1])])
        if not n is '\n':
            print n,
        elif n is temp[1]:
            print n
        temp[0], temp[1] = temp[1], n


data = read_data(FILE_NAME)
data = chunker(data)
analysis = analyze(data)
out_write(analysis)
