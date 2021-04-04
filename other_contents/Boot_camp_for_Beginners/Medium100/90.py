from itertools import accumulate

N, Q = map(int, input().split())
S = input()

AC_count = [0]
for i in range(N):
    temp = S[i: i + 2]
    if temp == "AC":
        AC_count.append(1)
    else:
        AC_count.append(0)

AC_count = list(accumulate(AC_count))

for _ in range(Q):
    l, r = map(int, input().split())
    ans = AC_count[r - 1] - AC_count[l - 1]
    print(ans)