import numpy as np
N, K = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype=np.int32)
K -= 1
ans = np.ceil((N-1)/K) 
print(ans)