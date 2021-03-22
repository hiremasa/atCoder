N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

import bisect

ans = 0
len_B = len(B)
for b in B:
    ans += bisect.bisect_left(A, b) * (len_B - bisect.bisect(C, b))
print(ans)