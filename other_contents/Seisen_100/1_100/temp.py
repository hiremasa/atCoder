A = [input() for _ in range(10)]
num_of_land = sum([1 for i in range(10) for j in range(10) if A[i][j] == "o"])

dx_dy=[[1,0], [-1,0], [0,1], [0,-1]]

for start_point in [(i, j) for i in range(10) for j in range(10)]:
    if A[start_point[0]][start_point[1]] == "o":
        continue
    
    #init
    cnt = 0
    visited = [[0] * 10 for _ in range(10)]
    work_stack = [start_point]
    visited[start_point[0]][start_point[1]] = 1

    #更新
    while work_stack:
        now_loc = work_stack.pop()

        for i in range(4):
            now_x = now_loc[0] + dx_dy[i][0]
            now_y = now_loc[1] + dx_dy[i][1]
            if 0 <= now_x < 10 and 0 <= now_y < 10 and visited[now_x][now_y] == 0 and A[now_x][now_y] == "o":
                work_stack.append([now_x, now_y])
                visited[now_x][now_y] = 1
                cnt += 1

    if cnt == num_of_land:
        exit(print("YES"))
print("NO")
