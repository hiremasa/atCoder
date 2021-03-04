N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

import numpy as np
A = np.array(A)
B = np.array(B)
cnt = 0
for i in range(N-1, -1, -1):
    a, b = A[i], B[i]
    _, q = divmod(a + cnt, b)
    cnt += (b - q)%b
print(cnt)

