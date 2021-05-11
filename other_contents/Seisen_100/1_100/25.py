from collections import deque
dx_dy = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()

    C = [list(map(int,input().split())) for _ in range(h)]
    L = [[0] * w for _ in range(h)]

    land_number = 1
    for i in range(h):
        for j in range(w):
            if C[i][j] == 0:
                continue
            if L[i][j] >= 1:
                continue

            #init
            L[i][j] = land_number
            stack = deque([[i, j]])

            #更新
            while stack:
                now_i, now_j = stack.pop()
                for di, dj in dx_dy:
                    next_i = now_i + di
                    next_j = now_j + dj
                    if 0 <= next_i < h and 0 <= next_j < w:
                        if C[next_i][next_j] == 1 and L[next_i][next_j] == 0:
                            L[next_i][next_j] = land_number
                            stack.append([next_i, next_j])
            land_number += 1
    print(land_number - 1)
