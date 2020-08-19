N=int(input())
L_list=list(map(int, input().split()))

ans=0

for i in range(N):
	for j in range(i, N):
		for k in range(j, N):
			if L_list[i]!= L_list[j] and L_list[j] != L_list[k] and L_list[k] != L_list[i]:
				if L_list[i]+L_list[j]> L_list[k] and L_list[j]+L_list[k]>L_list[i] and L_list[k]+L_list[i]>L_list[j]:
					ans+=1
print(ans)
