N, M = map(int, input().split())
XY = list([0] * N for _ in range(N))
for _ in range(M):
    x, y = map(int, input().split())
    XY[x - 1][y - 1] = 1
    XY[y - 1][x - 1] = 1

import itertools

for i in range(N, -1, -1):
    for comb in itertools.combinations(range(N), i):
        for c in itertools.combinations(comb, 2):
            if XY[c[0]][c[1]] == 0:
                break
        else:
            exit(print(i))
print(1)