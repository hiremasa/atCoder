import math
n,m=map(int,input().split())
s=input()
t=input()
ans=n*m//math.gcd(n,m)
if math.gcd(n,m)==1:
    if s[0]==t[0]:
        print(ans)
    else:
        print(-1)
else:
    tmp=math.gcd(n,m)
    for i in range(tmp):
        if s[n*i//tmp]!=t[m*i//tmp]:
            ans=-1
            break
    print(ans)
