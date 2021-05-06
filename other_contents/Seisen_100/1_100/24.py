N = int(input())
G = [[] for _ in range(N + 1)]

for _ in range(N):
    i, num, *nodes = map(int, input().split())
    G[i] = nodes

go_time = [0] * (N + 1)
back_time = [0] * (N + 1)

def DFS(node, t):
    #行きの記録
    t += 1
    go_time[node] = t
    for next_node in G[node]:
        if go_time[next_node] == 0:
            t = DFS(next_node, t)

    #帰りの記録
    t += 1
    back_time[node] = t
    return t

t = 0
for node in range(1, N + 1):
    if go_time[node] == 0:
        t = DFS(node, t)
    print(node, go_time[node], back_time[node])