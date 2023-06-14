def load_dataset():
    # Example dataset
    return [['bread', 'milk'],
            ['bread', 'diaper', 'beer', 'egg'],
            ['milk', 'diaper', 'beer', 'cola'],
            ['bread', 'milk', 'diaper', 'beer'],
            ['bread', 'milk', 'diaper', 'cola']]

def create_C1(dataset):
    # Create a list of unique items in the dataset
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))

def scan_dataset(dataset, candidates, min_support):
    # Count the support of each candidate itemset in the dataset
    itemset_counts = {}
    for transaction in dataset:
        for candidate in candidates:
            if candidate.issubset(transaction):
                itemset_counts[candidate] = itemset_counts.get(candidate, 0) + 1

    num_items = float(len(dataset))
    frequent_itemsets = []
    support_data = {}
    for itemset in itemset_counts:
        support = itemset_counts[itemset] / num_items
        if support >= min_support:
            frequent_itemsets.append(itemset)
        support_data[itemset] = support

    return frequent_itemsets, support_data

def generate_candidates(frequent_itemsets, k):
    # Generate candidate itemsets of size k from frequent itemsets of size k-1
    candidates = []
    num_frequent_itemsets = len(frequent_itemsets)
    for i in range(num_frequent_itemsets):
        for j in range(i + 1, num_frequent_itemsets):
            L1 = list(frequent_itemsets[i])[:k - 2]
            L2 = list(frequent_itemsets[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                candidates.append(frequent_itemsets[i] | frequent_itemsets[j])
    return candidates

def apriori(dataset, min_support):
    # Generate frequent itemsets using the Apriori algorithm
    C1 = create_C1(dataset)
    dataset = list(map(set, dataset))
    frequent_itemsets, support_data = scan_dataset(dataset, C1, min_support)
    all_frequent_itemsets = [frequent_itemsets]
    k = 2

    while len(all_frequent_itemsets[k - 2]) > 0:
        candidates = generate_candidates(all_frequent_itemsets[k - 2], k)
        frequent_itemsets_k, support_data_k = scan_dataset(dataset, candidates, min_support)
        support_data.update(support_data_k)
        all_frequent_itemsets.append(frequent_itemsets_k)
        k += 1

    return all_frequent_itemsets, support_data

# Example usage
dataset = load_dataset()
min_support = 0.4
frequent_itemsets, support_data = apriori(dataset, min_support)

# Print frequent itemsets and their support
for k, itemsets in enumerate(frequent_itemsets):
    print(f'Frequent Itemsets of Size {k + 1}:')
    for itemset in itemsets:
        print(f'{tuple(itemset)}: Support = {support_data[itemset]:.2f}')
    print()
