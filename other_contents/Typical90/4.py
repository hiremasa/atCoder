import sys
input = sys.stdin.readline
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [[0] * W for _ in range(H)]

row_list = [sum(A[i]) for i in range(H)]
col_list = [sum(A[i][j] for i in range(H)) for j in range(W)]


# for i in range(H):
#     for j in range(W):
#         B[i][j] = row_list[i] + col_list[j] - A[i][j]
ans = [[row_list[i] + col_list[j] - A[i][j] for j in range(W)] for i in range(H)]

for b in ans:
    print(*b)