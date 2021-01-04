H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

for x in range(H):
    for y in range(W):
        if S[x][y]=="#":
            flag = False
            for dx, dy in dx_dy:
                x_p = x + dx
                y_p = y + dy
                
                if 0 <= x_p < H and 0 <=y_p < W:
                    if S[x_p][y_p] == "#":
                        flag = True
            if not flag:
                exit(print("No"))
print("Yes")
