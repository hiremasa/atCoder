import heapq
N, M = map(int, input().split())
A = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(A)
for _ in range(M):
    temp_min = heapq.heappop(A)
    heapq.heappush(A, - (-temp_min // 2))
print(-sum(A))