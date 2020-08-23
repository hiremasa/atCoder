A, B, C, K = map(int, input().split())

if K<=A:
	print(1*K)
elif A<K<=A+B:
	print(1*A)
else:
	print(1*A-1*(K-A-B))