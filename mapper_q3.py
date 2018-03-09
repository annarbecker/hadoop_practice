# input data
# Date          Time    Store     Item   Cost   Payment
# 2012-01-01    12:01   San Jose  Music  12.99  Amex

# Find sales value across all the stores
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print "{0}\t{1}".format(store, cost)
