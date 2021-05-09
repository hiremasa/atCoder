N = int(input())
G = [[] for _ in range(N + 1)]

go_time = [0] * (N + 1)
back_time = [0] * (N + 1)

for _ in range(N):
    i, num, *nodes = map(int, input().split())
    G[i] = nodes


def dfs(node, t):
    #行きの処理
    t += 1
    go_time[node] = t

    #再帰処理
    for next_node in G[node]:
        if go_time[next_node] == 0:
            t = dfs(next_node, t)

    #帰りの処理
    t += 1
    back_time[node] = t

    return t

t = 0
for i in range(1, N + 1):
    if go_time[i] == 0:
        t = dfs(i, t)

for i in range(1, N + 1):
    print(i, go_time[i], back_time[i])