from collections import deque
h, w, n = map(int, input().split())
G = [input() for _ in range(h)]
num_loc = [[] for _ in range(n)]
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for i in range(h):
    for j in range(w):
        g = G[i][j]
        if g != "." or g != "X":
            if g == "S":
                init_loc = [i, j]
            elif g == "1" or g == "2" or g == "3" or g == "4" \
            or g == "5" or g == "6" or g == "7" or g == "8" or g == "9":
                num_loc[int(g) - 1] = [i, j]
#print(num_loc, init_loc, num_loc[0][0], num_loc[0][1])

def bfs(start_i, start_j, goal_i, goal_j):
    #ans = 0
    stack = deque([[start_i, start_j]])
    visited = [[0] * w for _ in range(h)]
    visited[start_i][start_j] = 1

    while stack:
        now_i, now_j = stack.popleft()
        for di, dj in dx_dy:
            next_i = now_i + di
            next_j = now_j + dj
            if 0 <= next_i < h and 0 <= next_j < w:
                if G[next_i][next_j] != "X" and visited[next_i][next_j] == 0:
                    #ans += 1
                    stack.append([next_i, next_j])
                    visited[next_i][next_j] = 1 + visited[now_i][now_j]
                    # if [next_i, now_j] == goal:
                    #     return ans
    return visited[goal_i][goal_j] - 1


ans = bfs(init_loc[0], init_loc[1], num_loc[0][0], num_loc[0][1])
for i in range(n - 1):
    ans += bfs(num_loc[i][0], num_loc[i][1], num_loc[i + 1][0], num_loc[i + 1][1])
print(ans)