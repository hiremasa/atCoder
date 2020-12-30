N=int(input())
A=list(map(int, input().split()))

ans = [0]*100003
for a in A:
    ans[a+1]+=1
    ans[a]+=1
    ans[a+2]+=1
print(max(ans))



#-------------------------

import numpy as np
# 前後1まで回収できる
N = int(input())

# n以下のものをかぞえる
A = np.bincount(np.array(input().split(), dtype=np.int32))

B = A.copy()  # そのままとる
B[1:] += A[:-1]  # 1増やして回収
B[:-1] += A[1:]  # 1減らして回収

answer = B.max()
print(answer)
