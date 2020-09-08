N=int(input())
A=list(map(int, input().split()))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a


#これだとTLEする
ans=0
for i in range(N):
	temp=0
	for idx, a in enumerate(A):
		if idx==i:
			continue
		temp=gcd(temp, a)
	ans=max(ans,temp)
print(ans)