N= int(input())
A = [int(input()) for _ in range(N)]
from collections import Counter

A = Counter(A)
ans = 0
for k, v in A.items():
    if v%2 != 0:
        ans += 1
print(ans)
