V, E, r = map(int, input().split())
G = [[] for i in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    G[s].append([t, d])

import heapq

def dijkstra(s):
    #init
    D = [float("inf")] * V
    D[s] = 0
    nodelist = [(0, s)]# (重みの和, ノード番号)
    #更新
    while nodelist:
        cost, node = heapq.heappop(nodelist)
        # if D[node] < cost:
        #     continue
        for next_node, next_cost in G[node]:
            if D[node] + next_cost < D[next_node]:
                D[next_node] = D[node] + next_cost
                heapq.heappush(nodelist, (D[next_node], next_node))
    return D
result = dijkstra(r)

for i in range(V):
    print(result[i] if result[i] < float("inf") else "INF")
