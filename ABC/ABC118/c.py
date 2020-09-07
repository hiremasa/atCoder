N=int(input())
A=list(map(int, input().split()))

def gcd(a,b):
	while b:
		a, b = b, a%b
	return a


ans=0
for a in A:
	ans=gcd(ans, a)
print(ans)