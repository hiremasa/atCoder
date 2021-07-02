N, M = map(int, input().split())
G = [[] for i in range(N)]
visited = [False] * N
for _ in range(M):
    s, t = map(int, input().split())
    G[s - 1].append(t - 1)
    G[t - 1].append(s - 1)

import heapq

def dfs(s, parent):
    is_tree = False

    # if visited[s]:
    #     return
    visited[s] = True

    for node in G[s]:
        if node != parent:
            if visited[node]:
                is_tree = True
                return is_tree
            else:
                is_tree |= dfs(node, s)
    return is_tree

ans = 0

for i in range(N):
    if visited[i]:
        continue
    if not dfs(i, -1):
        ans += 1
print(ans)