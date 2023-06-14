import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            self.bit_array[index] = 1

    def __contains__(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            if not self.bit_array[index]:
                return False
        return True

# Example usage
if __name__ == "__main__":
    def hash_function_1(item):
        return int(hashlib.md5(item.encode()).hexdigest(), 16)

    def hash_function_2(item):
        return int(hashlib.sha256(item.encode()).hexdigest(), 16)

    size = 100
    hash_functions = [hash_function_1, hash_function_2]

    bloom_filter = BloomFilter(size, hash_functions)

    # Add items to the filter
    bloom_filter.add("apple")
    bloom_filter.add("banana")
    bloom_filter.add("orange")

    # Check if items are in the filter
    print("apple" in bloom_filter)   # True
    print("banana" in bloom_filter)  # True
    print("orange" in bloom_filter)  # True
    print("grape" in bloom_filter)   # False
