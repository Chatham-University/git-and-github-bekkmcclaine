import random
import time
from collections import deque

class ArrayDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]
        print("The first few numbers are:")
        for num in self.nums[:6]:
            print(num)

class VectorDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]
        print("The first few numbers are:")
        for num in self.nums[:6]:
            print(num)

class LinkedListDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = deque(rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums))
        print("The first few numbers are:")
        for num in list(self.nums)[:6]:  # Convert deque to list for slicing
            print(num)

# Constants
HOW_MANY_NUMS = 10**6  # 10^6 = 1 million

# Random number generator with a fixed seed for reproducibility
rand = random.Random(5564011392837540628)

# Timing and execution
start = time.time()
ArrayDemo(HOW_MANY_NUMS, rand)
end = time.time()
print(f"Array Time: {end - start:.3f} seconds")

start = time.time()
VectorDemo(HOW_MANY_NUMS, rand)
end = time.time()
print(f"Vector Time: {end - start:.3f} seconds")

start = time.time()
LinkedListDemo(HOW_MANY_NUMS, rand)
end = time.time()
print(f"LinkedList Time: {end - start:.3f} seconds")



