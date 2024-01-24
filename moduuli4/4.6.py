import math
import random

n = 0
N = 10000000
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        n = n + 1
    i = i + 1

pii = (4 * n) / N
print(f"Piin likiarvo on: {pii:.6f}")