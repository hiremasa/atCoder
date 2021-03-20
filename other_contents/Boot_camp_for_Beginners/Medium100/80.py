N = int(input())
S = input()
mod = 10**9 + 7
from collections import defaultdict
dd = defaultdict(int)
for s in S:
    dd[s] += 1

ans = 1
for v in dd.values():
    ans *= (v + 1)
    ans % mod
print(ans- 1)