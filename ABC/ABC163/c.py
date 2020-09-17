from collections import defaultdict
N=int(input())
A=list(map(int, input().split()))
dd=defaultdict(int)
for i in range(1, N+1):
	dd[i]+=0
	if i>=2:
		dd[A[i-2]]+=1
for k, v in dd.items():
	print(v)

