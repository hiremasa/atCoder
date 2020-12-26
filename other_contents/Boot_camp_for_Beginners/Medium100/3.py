S= str(input())
ans = [0] * (len(S)+1)

for i in range(len(S)):
	if S[i]=="<":
		ans[i+1] += ans[i] +1

for i in range(len(S)-1, -1, -1):
	if S[i]==">":
		ans[i] = max(ans[i], ans[i+1]+1)

print(sum(ans))

#----------------------------------------------------------------------
from collections import Counter
left_count = Counter()  # Sのi番目まで読んだとき、連続している<の数
right_count = Counter() # Sのi番目まで読んだとき、連続している>の数
 
for i in range(0, len(S)):
    if S[i] == "<":
        left_count[i] = left_count[i-1] + 1
 
for i in range(len(S) - 1, -1, -1):
    if S[i] == ">":
        right_count[i] = right_count[i+1] + 1
 
# aについて
s = 0
for i in range(len(S)+1):
    # aのi文字目まで考えるときはleftはi+1でrightはi
    m = max(left_count[i-1], right_count[i])
    #print(i, left_count[i - 1], right_count[i], m)
    s += m
print(s)



