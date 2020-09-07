A, B , C = map(int, input().split())
def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

if A==1:
	print("YES")
elif C%gcd(A,B)==0:
	print("YES")
else:
	print("NO")