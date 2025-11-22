# Using List Comprehension
import math
n = 30
p = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1))]
print(p)