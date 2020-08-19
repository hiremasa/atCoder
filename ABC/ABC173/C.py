H, W, K =map(int, input().split())

arr= [list(input()) for _ in range(H)]
ans=0

for paint_h in range(2**H):
	for paint_w in range(2**W):
		cnt=0
		for i in range(H):
			for j in range(W):
				if (paint_h>>i)&1==0 and (paint_w>>j)&1==0:
					if arr[i][j]=="#":
						cnt+=1

		if cnt==K:
			ans+=1
print(ans) 