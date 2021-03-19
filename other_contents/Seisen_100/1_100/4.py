import numpy as np
N, M = map(int, input().split())

A = np.array([list(input().split()) for _ in range(N)], dtype = np.int32)
ans = 0
for i in range(M - 1):
    for j in range(i, M):
        total = 0
        for n in range(N):
            total += max(A[n, i], A[n, j])
            if ans < total:
                ans = total

print(ans)



#========================別解
import numpy as np
import itertools
 
N,M = map(int,readline().split())
A = np.array(read().split(),np.int64).reshape(N,M)
 
answer = 0
for i,j in itertools.combinations(range(M),2):
    x = np.sum(np.maximum(A[:,i],A[:,j]))
    if answer < x:
        answer = x
 
print(answer)
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np
import itertools

N,M = map(int,readline().split())
A = np.array(read().split(),np.int64).reshape(N,M)

answer = 0
for i,j in itertools.combinations(range(M),2):
    x = np.sum(np.maximum(A[:,i],A[:,j]))
    if answer < x:
        answer = x

print(answer)
