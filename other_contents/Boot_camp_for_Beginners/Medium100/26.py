n = int(input())
a = list(map(int, input().split()))
cnt = 1
dif = [a[i]-a[i-1] for i in range(1,n) if a[i]-a[i-1] != 0]
 
i = 1
maxi = len(dif)
while i < maxi:
  if dif[i]*dif[i-1] < 0:
    cnt += 1
    i += 2
  else:
    i += 1
    
print(cnt)