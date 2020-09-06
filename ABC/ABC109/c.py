#再帰
def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a%b)
#ループ
def gcd(a,b):
  while b:
    a,b = b,a%b
  return abs(a)

def solve(x_list):
	ans=0
	for x in x_list:
		ans=gcd(ans, x)
	return ans

N, X = map(int, input().split())
x_list=list(abs(int(x)-X) for x in input().split())

print(solve(x_list))