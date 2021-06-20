import sys
sys.setrecursionlimit(10**6)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

def dfs(s):
    D = [-1] * N
    D[s] = 0
    stk = [s]
    push, pop = stk.append, stk.pop
    while stk:
        v = pop()
        nd = D[v] + 1
        for nv in G[v]:
            if D[nv] >= 0: continue
            D[nv] = nd
            push(nv)
    return D

D0 = dfs(0)
mxi = max(enumerate(D0), key=lambda x: x[1])[0]
Dmx = dfs(mxi)
print(max(Dmx) + 1)
