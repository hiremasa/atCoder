import numpy as np
N = int(input())

y = 0
total = 0
while total < N:
    y += 1
    total += y

se = set([i for i in range(1, y + 1)]) - set([total - N])
print(*se)