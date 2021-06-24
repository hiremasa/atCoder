import heapq
V, E = map(int, input().split())

G = [[] for _ in range(V)]

for _ in range(E):
    s, t, w = map(int, input().split())
    G[s].append([w, t])
    G[t].append([w, s])


#init
pq = []
ans = 0
visited = [0] * V
for w, node in G[0]:
    heapq.heappush(pq, [w, node])
visited[0] = 1

while pq:
    w, node = heapq.heappop(pq)
    if visited[node] == 1:
        continue
    visited[node] = 1
    ans += w
    for next_w, next_node in G[node]:
        if visited[next_node]:
            continue
        heapq.heappush(pq, [next_w, next_node])


print(ans)
