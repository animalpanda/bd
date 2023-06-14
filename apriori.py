def apriori(dataset, min_support):
    items = sorted(list(set(item for transaction in dataset for item in transaction)))
    L = [[item] for item in items if sum([1 for transaction in dataset if set([item]).issubset(transaction)]) >= min_support]
    k = 2
    while L:
        L = [list(set(a + b)) for a in L for b in L if len(set(a + b)) == k and sum([1 for transaction in dataset if set(a + b).issubset(transaction)]) >= min_support]
        k += 1
    return L

# Input dataset
dataset = [
    ['bread', 'milk'],
    ['bread', 'diapers', 'beer', 'eggs'],
    ['milk', 'diapers', 'beer', 'cola'],
    ['bread', 'milk', 'diapers', 'beer'],
    ['bread', 'milk', 'diapers', 'cola']
]

# Minimum support threshold
min_support = 2

# Run Apriori algorithm and print frequent itemsets
frequent_itemsets = apriori(dataset, min_support)
for itemset in frequent_itemsets:
    print(itemset)
