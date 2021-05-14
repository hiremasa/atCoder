from collections import deque
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

G = [input() for _ in range(R)]
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[-1] * C for _ in range(R)]
stack = deque([[sy - 1, sx - 1]])
visited[sy - 1][sx - 1] = 0

while stack:
    now_y, now_x = stack.popleft()
    for dx, dy in dx_dy:
        next_dx = now_x + dx
        next_dy = now_y + dy
        if 0 <= next_dy < R and 0 <= next_dx < C:
            if G[next_dy][next_dx] != "#" and visited[next_dy][next_dx] == -1:
                visited[next_dy][next_dx] = visited[now_y][now_x] + 1
                stack.append([next_dy, next_dx])
print(visited[gy - 1][gx - 1])