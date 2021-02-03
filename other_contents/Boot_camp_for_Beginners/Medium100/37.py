import numpy as np
N = int, input().split()
H = np.array(input().split(), dtype=np.int32)


def F(L,R):
    if R < L:
        return 0
    idx = L + H[L:R+1].argmin()
    x = H[idx]
    H[L:R+1] -= x
    return x + F(L,idx-1) + F(idx+1,R)

answer = F(0,N-1)
print(answer)