N=int(input())
from collections import deque
P=deque(list(map(int, input().split())))

min_v=P.popleft()
cnt=1
while P:
	temp=P.popleft()
	if temp<=min_v:
		cnt+=1
		min_v=temp

print(cnt)
