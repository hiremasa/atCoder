N = int(input())

XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])

D = [[0] * N for _ in range(N)]
for i in range(N - 1):
    for j in range(N):
        d = ((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2) ** 0.5
        D[i][j] = d
        D[j][i] = d

import itertools
import math
ans = 0
for root in itertools.permutations([i for i in range(N)]):
    ans += sum([D[root[i]][root[i+1]] for i in range(N-1)])
print(ans/math.factorial(N))