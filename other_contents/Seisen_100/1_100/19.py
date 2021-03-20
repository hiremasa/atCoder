D = int(input())
N = int(input())
M = int(input())
ds = [0]+ sorted([int(input()) for _ in range(N - 1)]) + [D]#: 店舗の位置
ks = sorted([int(input()) for _ in range(M)]) #: 宅配先の位置
def is_ok(d_idx, k):
    return ds[d_idx] <= k

def meguru_bisect(k, ok, ng):
    while abs(ng-ok)>1:
        mid = (ok + ng) // 2
        if is_ok(mid, k):
            ok = mid
        else:
            ng = mid
    return min(k - ds[ok], ds[ok + 1] - k)

ans = 0
for k in ks:
    ans += meguru_bisect(k, ok = -1, ng = len(ds))
print(ans



#================================

import bisect
D = int(input())
N = int(input())
M = int(input())
ds = [0]+ sorted([int(input()) for _ in range(N - 1)]) + [D]#: 店舗の位置
ks = sorted([int(input()) for _ in range(M)]) #: 宅配先の位置