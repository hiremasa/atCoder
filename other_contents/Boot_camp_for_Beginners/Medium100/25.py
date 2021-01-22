N, K = map(int, input().split())
A = list(input().split())

from collections import Counter

B = sorted(Counter(A).items(), key=lambda x:x[1]) #valueでsort
ans = 0
for i in range(max(0, len(B) - K)):
    ans += B[i][1]
print(ans)