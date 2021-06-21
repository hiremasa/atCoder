import sys
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

def dfs(s):
    stack = [s]
    D = [-1] * N
    D[s] = 0

    while stack:
        node = stack.pop()
        for next_node in G[node]:
            if D[next_node] == -1:
                D[next_node] = D[node] + 1
                stack.append(next_node)
    return D

# def dfs(s):

#     for next_node in G[s]:
#         if D[next_node] == -1:
#             dfs(next_node)

u = max(enumerate(dfs(0)), key=lambda x: x[1])[0]
ans = max(dfs(u)) + 1
print(ans)


#木かどうか判定
def dfs(now,prev):
  global flag
  for next in g[now]:
    if next!=prev:
      if memo[next]:
        flag=False
      else:
        memo[next]=True
        dfs(next,now)