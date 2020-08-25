import heapq
N, M =map(int, input().split())
A=list(map(lambda x: int(x)*(-1), input().split())) #各要素を-1倍
heapq.heapify(A) #Aを優先度付きキューに

for _ in range(M):
	temp_min=heapq.heappop(A)
	heapq.heappush(A, (-1)*(temp_min*(-1)//2))
print(-sum(A))
