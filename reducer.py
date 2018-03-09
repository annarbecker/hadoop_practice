import sys
# Data from mapper
# Store     Sale
# San Jose  12.99

# Key: store name, Value: sale amount
salesTotal = 0
oldStore = None

# Loop through the data which is in key \t value format
# All the sales for a particular store will be presented, then the key will change and we'll move on to the next store
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Bad data, skip this line
        continue

    store, sale = data
    sale = float(sale)

    if oldStore and oldStore != store:
        print "{0}\t{1}".format(oldStore, salesTotal)
        oldStore = store
        salesTotal = 0

    oldStore = store

    # Find highest individual sale for each separate store
    if sale > salesTotal:
        salesTotal = sale

    if oldStore != None:
        print "{0}\t{1}".format(oldStore, salesTotal)
