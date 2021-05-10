#=================スタック==================
from collections import deque
N, Q = map(int, input().split())

dd = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    dd[a - 1].append(b - 1)
    dd[b - 1].append(a - 1)


count = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    count[p - 1] += x



# init
visited = [0] * N
stacked_v = deque([0])

#dfs
while stacked_v:
    now_v = stacked_v.pop()
    visited[now_v] = 1

    for next_v in dd[now_v]:
        if visited[next_v] == 0:
            count[next_v] += count[now_v]
            stacked_v.append(next_v)

print(*count)


#====================再帰======================
from sys import setrecursionlimit
setrecursionlimit(10**7)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(N - 1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  G[a].append(b)
  G[b].append(a)

count = [0] * N
for _ in range(Q):
  p, x = map(int, input().split())
  count[p - 1] += x

def DFS(cur_node, prev_node):
  for next_node in G[cur_node]:
    if next_node == prev_node: continue
    count[next_node] += count[cur_node]
    DFS(next_node, cur_node)
      
DFS(0, -1)
print(*count)
  
