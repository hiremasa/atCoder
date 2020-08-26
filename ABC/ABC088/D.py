from collections import deque

H, W = map(int, input().split())
C=list(list(input()) for _ in range(H))

def bfs():
	sx, sy= 0, 0
	gx, gy= H-1, W-1
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	work_queue=deque([])
	work_queue.append((sx, sy))
	visited=[[float("inf")]*W for _ in range(H)]
	visited[sx][sy]=1

	while work_queue:
		x, y = work_queue.popleft()

		for i in range(4):
			nx, ny = x+dx[i], y+dy[i]

			if 0<=nx<H and 0<=ny<W and visited[nx][ny]==float("inf") and C[nx][ny]!="#":
				work_queue.append((nx, ny))
				visited[nx][ny]= visited[x][y]+1
	return visited[gx][gy]


temp=bfs()

black=0
white=0
for i in range(H):
	for j in range(W):
		if C[i][j]==".":
			white+=1
		else:
			black+=1

if temp==float("inf"):
	print(-1)
else:
	print(white-temp)




