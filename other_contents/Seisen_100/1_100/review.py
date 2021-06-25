import heapq
V, E, r = map(int, input().split())

G = [[] for _ in range(V)]

for _ in range(E):
    s, t, w = map(int, input().split())
    G[s].append([w, t])
    G[t].append([w, s])


#init
pq = []
Distance = [float("inf")] * V
heapq.heappush(pq, [0, r])
Distance[r] = 0

while pq:
    w, node = heapq.heappop(pq)
    Distance[node] = w
    if Distance[node] < w:
        continue
    for next_w, next_node in G[node]:
        if Distance[next_node] > Distance[node] + next_w:
            heapq.heappush(pq, [Distance[node] + next_w, next_node])
print(*Distance)





# while pq:
#     w, node = heapq.heappop(pq)
#     if visited[node] == 1:
#         continue
#     visited[node] = 1
#     ans += w
#     for next_w, next_node in G[node]:
#         if visited[next_node]:
#             continue
#         heapq.heappush(pq, [next_w, next_node])


# print(ans)
