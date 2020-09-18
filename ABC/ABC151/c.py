N, M = map(int, input().split())

wa=[0]*N
ac=[False]*N
for i in range(M):
	p, S = input().split()
	p=int(p)-1
	
	if S=="AC":
		ac[p]=True

	else:#一度ACしたらWAをカウントしない
		if not ac[p]:
			wa[p]+=1

a=0
b=0

for i in range(N):
	if ac[i]:
		a+=1
		b+=wa[i]
print(*[a,b])
