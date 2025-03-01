import random
from collections import deque

class LinkedListDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = deque(rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums))

        print("The first few numbers are:")
        for num in list(self.nums)[:6]:  # Convert deque to list for slicing
            print(num)

# Example usage
rand = random.Random()
demo = LinkedListDemo(10, rand)

