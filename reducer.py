import sys

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

    thisStore, thisSale = data
    thisSale = float(thisSale)

    if oldStore and oldStore != thisStore:
        print "{0}\t{1}".format(oldStore, salesTotal)
        oldStore = thisStore
        salesTotal = 0

    oldStore = thisStore

    # Find highest individual sale for each separate store
    if thisSale > salesTotal:
        salesTotal = thisSale

    if oldStore != None:
        print "{0}\t{1}".format(oldStore, salesTotal)
