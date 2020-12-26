H, W = map(int, input().split())
S=[input() for _ in range(H)]

"""
import itertools
for dx,dy in itertools.product([-1,0,1],repeat=2):
とするほうがベター
"""
dxdy = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0, -1), (1,-1)]
ans = list([0]*W for _ in range(H))


for i in range(H):
	for j in range(W):
		if S[i][j] == "#":
			ans[i][j] = "#"
		else:
			temp = 0
			for dx, dy in dxdy:
				if 0<=i+dx<H and 0<=j+dy<W:
					if S[i+dx][j+dy] =="#":
						temp+=1
			ans[i][j]=temp

for i in range(H):
	print(*ans[i], sep="")
