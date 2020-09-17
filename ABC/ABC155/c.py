N=int(input())
S=list(input() for _ in range(N))

from collections import Counter

cnt=Counter(S)
max_cnt=cnt.most_common()[0][1]
ans=[name for name, cnt in cnt.items() if max_cnt==cnt]
print(*sorted(ans), sep="\n") #こう書くのがベター



"""
ans=[]
for k, v in cnt.items():
	if v!=max_cnt:
		continue
	ans.append(k)

for i in sorted(ans):
	print(i)
	
"""
