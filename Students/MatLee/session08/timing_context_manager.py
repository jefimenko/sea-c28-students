# -*- coding: utf-8 -*-
import sys
import time

class timed_manager(object):

    def __init__(self, something_filelike=None):
        self.something_filelike = something_filelike

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        log = u'Elapsed time: {0}\n'.format(elapsed)

        # Only allow writing/creating a log of times if a given input
        # is a string that ends in '.txt'. Defaults to writing to consoleWill
        # using sys.stdout if no valid filename determined.
        # Will break if given non-string input.
        if (self.something_filelike 
                and u'.txt' in self.something_filelike[-4:]):
            # Create/open a log and write to the file.
            with open(self.something_filelike, 'a') as f:
                f.write(log)
            print log
        else:
            sys.stdout.write(log)
        return False
