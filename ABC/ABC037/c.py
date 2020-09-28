import numpy as np
N, K = map(int, input().split())
A=np.array(input().split(), dtype=np.int64)

coef=np.zeros_like(A)
coef[:(N-K+1)]+=1

if N>K:
  coef[-(N-K):] -= 1
coef=coef.cumsum()
answer = (A*coef).sum()
print(answer)