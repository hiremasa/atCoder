def gcd(a,b):
	while b:
		a,b = b,a%b
	return abs(a)

K=int(input())

#余裕でTLE? -> しなかったAC

ans=0
for a in range(1, K+1):
	for b in range(1, K+1):
		for c in range(1, K+1):
			temp=a
			temp=gcd(temp, b)
			temp=gcd(temp, c)
			ans+=temp
print(ans)
