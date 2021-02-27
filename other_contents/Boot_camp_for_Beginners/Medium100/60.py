import itertools
from collections import defaultdict
N = int(input())
#S = [input() for _ in range(N)]

dd = defaultdict(int)
for chap in ["M", "A", "R", "C", "H"]:
    dd[chap] = 0
for _ in range(N):
    s = input()
    s_0 = s[0]
    if s_0 in ["M", "A", "R", "C", "H"]:
        dd[s_0] += 1


Chap_list = list(itertools.combinations(["M", "A", "R", "C", "H"], 3))

ans = 0
for chap_3 in Chap_list:
        ans += dd[chap_3[0]] * dd[chap_3[1]] * dd[chap_3[2]]
print(ans)