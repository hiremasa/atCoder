N, X = map(int, input().split())
A = list(map(int, input().split()))

from math import gcd

A = [abs(a - X) for a in A]
ans = A[]
for a in A:
    ans = gcd(ans, a)
print(ans)