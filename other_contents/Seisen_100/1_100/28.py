from collections import deque
n = int(input())
G = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
distance = [0] * (n + 1)
for i in range(n):
    u, k, *v = map(int, input().split())
    G[u] = v

#init
stack = deque([1])
visited[1] = 1

#更新
while stack:
    cur_node = stack.popleft()

    for next_node in G[cur_node]:
        if visited[next_node] != 0:
            continue
        distance[next_node] = distance[cur_node] + 1
        visited[next_node] = 1
        stack.append(next_node)

for i in range(1, n + 1):
    print(i, distance[i])