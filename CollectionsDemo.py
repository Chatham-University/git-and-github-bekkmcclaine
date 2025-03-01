import random
import time
from collections import deque

class ArrayDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]
        #print("The first few numbers are:")
        #for num in self.nums[:6]:
        #    print(num)
        # Commented out to remove the print statements for the first few numbers

class VectorDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]
        #print("The first few numbers are:")
        #for num in self.nums[:6]:
        #    print(num)
        # Commented out to remove the print statements for the first few numbers

class LinkedListDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = deque(rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums))
        #print("The first few numbers are:")
        #for num in list(self.nums)[:6]:  # Convert deque to list for slicing
        #    print(num)
        # Commented out to remove the print statements for the first few numbers

# Function to measure execution time
def measure_time(data_structure, how_many_nums, rand):
    start = time.time()
    data_structure(how_many_nums, rand)
    return time.time() - start

# Set increments for sizes
sizes = [10**3, 2 * 10**3, 5 * 10**3,
         10**4, 2 * 10**4, 5 * 10**4,
         10**5, 2 * 10**5, 5 * 10**5, 10**6] # 20 values from 10^3 to 10^6

# Random number generator with a fixed seed
rand = random.Random(5564011392837540628)

# Print header
print("Size\tArray Time (s)\tVector Time (s)\tLinkedList Time (s)")

# Run tests for each size and print results
for size in sizes:
    array_time = measure_time(ArrayDemo, size, rand)
    vector_time = measure_time(VectorDemo, size, rand)
    linkedlist_time = measure_time(LinkedListDemo, size, rand)

    # Print results in a tabular format
    print(f"{size}\t{array_time:.6f}\t{vector_time:.6f}\t{linkedlist_time:.6f}")


