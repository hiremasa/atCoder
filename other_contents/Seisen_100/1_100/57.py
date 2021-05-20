import heapq
N, K = map(int, input().split())

G = [[] for _ in range(N)]

def dijkstra(s, t):
    #init
    D = [float("inf")] * N
    D[s] = 0
    nodelist = [(0, s)]# (重みの和, ノード番号)
    while nodelist:
        cost, node = heapq.heappop(nodelist)

        for next_node, next_cost in G[node]:
            if D[next_node] < cost:
                continue
            for next_node, next_cost in G[node]:
                if D[node] + next_cost < D[next_node]:
                    D[next_node] = D[node] + next_cost
                    heapq.heappush(nodelist, (D[next_node], next_node))
    return D[t]


for _ in range(K):
    flag, *info = map(int, input().split())
    if flag:
        c, d, e = info
        G[c - 1].append([d - 1, e])
        G[d - 1].append([c - 1, e])
    else:
        a, b = info
        ans = dijkstra(a - 1, b - 1)
        print(ans if ans < float("inf") else -1)

