import sys
# Data from mapper
# Store     Sale
# San Jose  12.99

salesTotal = 0
totalNumberOfSales = 0

# Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    store, sale = data
    salesTotal += float(sale)
    totalNumberOfSales += 1

    print "{0}\t{1}".format(salesTotal, totalNumberOfSales)
