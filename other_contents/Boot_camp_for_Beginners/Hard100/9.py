import numpy as np
N, M = map(int, input().split())

A = np.array([list(input()) for _ in range(N)])
B = np.array([list(input()) for _ in range(M)])

h, w = B.shape

for i in range(N - h + 1):
    for j in range(N - w + 1):
        A_p = A[i:i+h, j:j+w]
        if np.all(A_p == B):
            exit(print("Yes"))
print("No")