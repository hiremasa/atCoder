N = int(input())
ans = 1
import math
for _ in range(N):
    t = int(input())
    ans = ans * t //math.gcd(ans, t)
print(ans)
