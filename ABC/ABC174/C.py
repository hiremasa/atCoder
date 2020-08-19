
K=int(input())
a_i=7%K
i=1
if a_i==0:
	exit(print(1))
while True:
	i+=1
	a_i=(10*a_i+7)%K
	if a_i==0:
		print(i)
		exit()
	if i>=K:
		print(-1)
		exit()


