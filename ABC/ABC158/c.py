A, B = map(int, input().split())

#A<= x*0.08 <A+1
#B<= x*0.10 <B+1

x=int(B*10)
while x<10*(B+1):
	if A<=x*0.08 and x*0.08<A+1:
		print(x)
		exit()
	x+=1
print(-1)

