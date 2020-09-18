H, N = map(int, input().split())

A=[]
B=[]
for _ in range(N):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

dp=[[float("inf")]*(H+1) for _ in range(N+1)]
dp[0][0]=0
for i in range(N):
	a, b = A[i], B[i]
	for j in range(H+1):
		if a>=j:
			dp[i+1][j] = min(dp[i][j], b)
		else:
			dp[i+1][j] = min(dp[i][j], dp[i+1][j-a]+b)
print(dp[-1][-1])
