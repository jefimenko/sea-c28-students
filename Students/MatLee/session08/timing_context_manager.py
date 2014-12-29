# -*- coding: utf-8 -*-
import sys
import time

class timed_manager(object):

    def __init__(self, something_filelike=sys.stdout):
        self.something_filelike = something_filelike

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        log = u'Elapsed time: {0}\n'.format(elapsed)

        # Attempt writing log to a file-like object.
        try:
            self.something_filelike.write(log)
            print log
        except AttributeError:
            print u'Object given is not file-like.'
            sys.stdout.write(log)
        return False
