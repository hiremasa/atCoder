N, M =map(int, input().split())
H=list(map(int, input().split()))

A=[True]*N

for i in range(M):
	a, b = map(int, input().split())

	if H[a-1]>H[b-1]:
		A[b-1]=False
	elif H[a-1]==H[b-1]:
		A[a-1]=False
		A[b-1]=False
	elif H[a-1]<H[b-1]:
		A[a-1]=False

print(sum(A))


