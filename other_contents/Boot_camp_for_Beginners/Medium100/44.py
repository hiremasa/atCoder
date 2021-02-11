import numpy as np
N = int(input())
A = input().split()

"""
if N%2 == 0: 
    ans = np.r_(A[::2][::-1] + A[1::2])
else:
    ans = np.r_(A[1::2][::-1] + A[::2])
"""
ans = A[::2][::-1] + A[1::2]
if not N&1:
  ans = ans[::-1]
print(*ans,sep=' ')