import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N = int(readline())
A = np.array(read().split(), np.int64)
counter = np.bincount(A)

total = (counter * (counter - 1)).sum() // 2
answer = (total - (counter - 1))[A]

print('\n'.join(answer.astype(str)))

