N=int(input())
ans=0
for j in range(1, N+1):
  Y=N//j
  ans+=Y*(Y+1)*j//2
print(ans)