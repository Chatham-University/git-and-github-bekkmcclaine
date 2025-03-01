import random

class VectorDemo:
    def __init__(self, how_many_nums, rand):
        self.nums = [rand.randint(0, how_many_nums - 1) for _ in range(how_many_nums)]

        print("The first few numbers are:")
        for num in self.nums[:6]:
            print(num)

# Example usage
rand = random.Random()
demo = VectorDemo(10, rand)

