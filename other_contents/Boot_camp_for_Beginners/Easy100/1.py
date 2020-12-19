A, B = map(int, input().split())
kuti=1
ans=0
while True:
  if kuti>=B:
    break
  kuti-=1
  kuti+=A
  ans+=1
print(ans)