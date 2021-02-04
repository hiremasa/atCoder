N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(int)

for d in D:
    dd[d] += 1
for t in T:
    dd[t] -= 1

ans = "YES" if min(dd.values()) >= 0 else "NO"
print(ans)