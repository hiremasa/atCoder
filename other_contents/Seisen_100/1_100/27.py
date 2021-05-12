from collections import deque
import copy
M = int(input())
N = int(input())

C = [list(map(int, input().split())) for _ in range(N)]
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for i in range(N):
    for j in range(M):
        G = copy.deepcopy(C)
        if G[i][j] == 0:
            continue
        #init
        stack = [[[i, j], set()]]

        #更新
        while stack:
            [now_i, now_j], history = stack.pop()
            ans = max(ans, len(history))
            for di, dj in dx_dy:
                next_i = now_i + di
                next_j = now_j + dj
                if 0 <= next_i < N and 0 <= next_j < M:
                    if G[next_i][next_j] == 1 and not((next_i, next_j) in history):
                        stack.append([[next_i, next_j], history | {(next_i, next_j)}])
print(ans)



#============================================
#https://qiita.com/rudorufu1981/items/e39aa16d73615c7e589f
import itertools,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
m = I()
n = I()
area = [LI() for _ in range(n)]
ans = 0
dndm = [[1,0],[-1,0],[0,1],[0,-1]]
stack = [] #スタック時の位置、過去の履歴
def dfs(i,j):
    global ans
    stack.append([[i,j],set()])
    while stack:
        [sn,sm],history = stack.pop()
        ans = max(ans,len(history))
        for dn,dm in dndm:
            nn,nm = sn+dn,sm+dm
            if not(0<=nn<=n-1) or not(0<=nm<=m-1) or area[nn][nm]==0 or ((nn,nm) in history):
                continue
            stack.append([[nn,nm],history | {(nn,nm)}])
for i,j in itertools.product(range(n),range(m)):
    if area[i][j]==1:
        dfs(i,j)
print(ans)