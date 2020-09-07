N=int(input())
T=list(int(input()) for _ in range(N))

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

answer = 1
for _ in range(N):
  x = int(input())
  answer *= x//gcd(answer, x)


print(ans)