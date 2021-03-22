import numpy as np
N = int(input())
A = np.array([input().split()], dtype=np.int32)
y = np.round(np.sum(A)/N)
ans = np.sum((A - y) ** 2)
print(int(ans))

