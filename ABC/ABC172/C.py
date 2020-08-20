
N, M, K = map(int, input().split())
A_list=list(map(int, input().split()))
B_list=list(map(int, input().split()))

import itertools
A_acum=list(itertools.accumulate(A_list))
B_acum=list(itertools.accumulate(B_list))
A_acum.insert(0, 0)
B_acum.insert(0, 0)


"""
A_acum=[0]
B_acum=[0]
for i in range(1, N+1):
	A_acum[i]=A_acum[i-1]+A_list[i-1]
for j in range(1, M+1):
	B_acum[i]=B_acum[i-1]+B_list[i-1]
"""
ans=0
j=M
for i in range(len(A_acum)): #iは読んだAの本の数
	if K<A_acum[i]:
		break
	res = K - A_acum[i] #残り時間

	while res<B_acum[j] and j>0:
		j-=1

	ans=max(ans, i+j)

print(ans)



