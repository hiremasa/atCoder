"""
X, K , D = map(int, input().split())

ans=1e+15

for i in range(K):
	init_X=X
	init_X+=i*D-(K-i)*D
	if abs(init_X)<ans:
		ans=abs(init_X)

print(ans)
"""
X, K , D = map(int, input().split())

left=X-K*D
right=X+K*D

if left<0<right:
	k=abs(X)//D
	X-=D * k
	print(X if (K-k)%2==0 else abs(X-D))

elif right<=0:
	print(-right)
else:
	print(left)