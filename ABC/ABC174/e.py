from math import ceil
N, K =map(int, input().split())
A=list(map(int, input().split()))


def is_ok(X):
	cnt=0
	for a in A:
		if a<=X:
			continue
		cnt+=ceil(a/X) -1
	return cnt<=K


"""
これはダメ -> なんで？
B=[-i for i in A]
heapq.heapify(B)
def is_ok(X):
	C=B.copy()
	for _ in range(K):
		max_a = heapq.heappop(C)
		temp=max_a/2
		heapq.heappush(C, temp)
		heapq.heappush(C, temp)
	tmp=heapq.heappop(C)
	return -tmp<=X
"""


def meguru_bisect(ng, ok):
	while abs(ng-ok)>1:
		mid = (ng+ok)//2
		if is_ok(mid):
			ok=mid
		else:
			ng=mid
	return ok

print(ceil(meguru_bisect(0, 1e+10)))


