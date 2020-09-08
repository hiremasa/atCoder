N=int(input())
A=list(map(int, input().split()))

cnt=0
for a in A:
	i=0
	while a % 2==0:
		a/=2
		i+=1
	cnt+=i
print(cnt)