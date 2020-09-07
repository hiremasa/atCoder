N=int(input())
T=list(int(input()) for _ in range(N))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

ans=T[0]
for i in range(1, N):
	ans=ans*T[i]//gcd(ans, T[i])
print(ans)