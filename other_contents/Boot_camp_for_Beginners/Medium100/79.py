N,M = map(int,input().split())
MOD = 10**9 + 7

fact = [1]
for i in range(1, N+M+1):
  fact.append((fact[-1] * i) % MOD)

x = fact[N] * fact[M]

if N == M:
  answer = 2 * x % MOD
elif abs(N-M) == 1:
  answer = x % MOD
else:
  answer = 0

print(answer)