S= str(input())

cur_pos = 0
ans = 0
for idx in range(len(S)):
	if S[idx]=="W":
		ans += idx - cur_pos
		cur_pos += 1

print(ans)