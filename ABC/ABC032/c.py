#しゃくとり法
#1. 条件を満たす限り右端を進める
#2. 条件を満たさなくなったら左端を条件を満たすまで進める
#注.左端と右端が同じ位置に来たときは右端も同時に進める
N, K = map(int, input().split())
S=[int(input()) for _ in range(N)]

if 0 in S:
	exit(print(N))


r, ans, temp=0,0,1

for l in range(N):
	while r<N and temp*S[r]<=K:
		temp*=S[r]
		r+=1
	ans=max(ans, r-l)
	if l==r:
		r+=1
	else:
		temp//=S[l]

print(ans)