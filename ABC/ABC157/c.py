N, M = map(int, input().split())
from collections import defaultdict, Counter
dd=defaultdict(int)
dd_count=defaultdict(int)
Flag=False #s=1 and c=0となる値があるかどうか
for _ in range(M):
	s, c = map(int, input().split())

	if N>=2 and s==1 and c==0:
		Flag=True

	#異なるものが2個以上ある
	if dd_count[s-1]>=1 and dd[s-1]!=c:
		exit(print(-1))
	else:
		dd[s-1]=c
		dd_count[s-1]+=1
	
if N>=2 and dd[0]==0 and not Flag:
	ans=10**(N-1)
	for i in range(1,N):
		ans+=dd[i]*10**(N-i-1)
	exit(print(ans))

if N>=2 and Flag:
	exit(print(-1))
else:
	ans=0
	for i in range(N):
		ans+=dd[i]*10**(N-i-1)
	print(int(ans))
