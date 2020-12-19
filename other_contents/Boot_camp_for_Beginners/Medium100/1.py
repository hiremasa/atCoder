N=int(input())
A=[int(input())-1 for _ in range(N)]


ans = 0
cur_idx = 0
for _ in range(N):

	cur_idx = A[cur_idx]
	ans+=1
	if cur_idx==1:
		print(ans)
		exit()
	

exit(print(-1))

