# input data
# Date          Time    Store     Item   Cost   Payment
# 2012-01-01    12:01   San Jose  Music  12.99  Amex

# Find total sales by producs category across all stores
# Key: item
# Value: cost

# Group data by product to find total sales for each product
import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tabe and put the data in an array
        data = line.strip().split("\t")

        # handle unexpected data (if the line doesn't include the expected 6 entries, ignore it)
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            # print the data that will be passed to the reducer
            print "{0}\t{1}".format(item, cost)
