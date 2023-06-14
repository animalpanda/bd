from itertools import combinations
from collections import defaultdict

def pcy_algorithm(dataset, min_support, hash_table_size):
    item_counts = defaultdict(int)
    hash_table = [0] * hash_table_size

    for transaction in dataset:
        for item in transaction:
            item_counts[item] += 1

    frequent_buckets = set()
    for item, count in item_counts.items():
        if count >= min_support:
            frequent_buckets.add(item)

    for transaction in dataset:
        pairs = combinations(sorted([item for item in transaction if item in frequent_buckets]), 2)
        for pair in pairs:
            hash_value = hash(pair) % hash_table_size
            hash_table[hash_value] += 1

    frequent_itemsets = []
    for item, count in item_counts.items():
        if count >= min_support:
            frequent_itemsets.append([item])

    for transaction in dataset:
        pairs = combinations(sorted([item for item in transaction if item in frequent_buckets]), 2)
        for pair in pairs:
            hash_value = hash(pair) % hash_table_size
            if hash_table[hash_value] >= min_support:
                frequent_itemsets.append(list(pair))

    return frequent_itemsets

dataset = [
    ['bread', 'milk'],
    ['bread', 'diapers', 'beer', 'eggs'],
    ['milk', 'diapers', 'beer', 'cola'],
    ['bread', 'milk', 'diapers', 'beer'],
    ['bread', 'milk', 'diapers', 'cola']
]

# Parameters
min_support = 2
hash_table_size = 10

# Run PCY algorithm
frequent_itemsets = pcy_algorithm(dataset, min_support, hash_table_size)

# Print the frequent itemsets
for itemset in frequent_itemsets:
    print(itemset)
