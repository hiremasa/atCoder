N=int(input())
S=str(input())



max_cnt = 0

for i in range(1,N):
	left_S=S[:i]
	right_S=S[i:]
	cnt = 0

	both = set(left_S) & set(right_S)

	if len(both) > max_cnt:
		max_cnt = len(both)

print(max_cnt)

