import numpy as np
import itertools
import bisect
N = int(input())
A = np.array(input().split(), dtype=np.int32)
B = np.array(input().split(), dtype=np.int32)

diff = A - B

lack = - diff[diff<0]
remain = diff[diff>0]

x = lack.sum()
remain.sort()
cum = remain[::-1].cumsum()
y = 0 if x == 0 else np.searchsorted(cum,x) + 1

answer = len(lack) + y if y <= len(remain) else -1

print(answer)
"""
print(diff)
if len(diff[diff >= 0]) == N:
    print(0)
elif sum(diff) < 0:
    print(-1)
else:
    neg = diff[diff < 0]
    pos = diff[diff > 0]

    if sum(pos) > sum(neg):
        pos_acc = list(itertools.accumulate(sorted(pos, reverse=True)))
        idx = bisect.bisect(pos_acc, abs(sum(neg)))
        print(idx + 1 + len(neg))
    else:
        neg_acc = list(itertools.accumulate(sorted(- neg, reverse=True)))
        idx = bisect.bisect(neg_acc, sum(pos))
        print(idx + 1 + len(pos))
"""