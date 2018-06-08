#!/usr/bin/env python
"""mapper.py"""

import sys
import nltk

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    pos_tuple = nltk.pos_tag(words)

    for word in pos_tuple:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        pos = word[1]

        print('%s\t%s' % (pos, 1))

