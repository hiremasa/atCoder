N, K = map(int, input().split())
H=list(map(int, input().split()))
if K>=N: exit(print(0))
import heapq
H=[-i for i in H]
heapq.heapify(H)

for i in range(K):
	heapq.heappop(H)
print(-sum(H))