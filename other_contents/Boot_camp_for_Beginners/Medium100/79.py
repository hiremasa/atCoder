N,M = map(int,input().split())
mod = 10**9 + 7
import math
if N == M:
    ans = (math.factorial(N%mod) * math.factorial(M%mod) * 2) % mod
elif abs(N - M) == 1:
    ans =  (math.factorial(N%mod) * math.factorial(M%mod)) % mod
else:
    ans = 0
print(ans)