from collections import Counter
N=int(input())
mod=1000000000 + 7

#nを素因数分解したリストを返す
def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


prime_table=[]
for i in range(2, N+1):
  prime_table+=(prime_decomposition(i))

prime_table=Counter(prime_table)
ans=1
for k, v in prime_table.items():
  ans*=(v+1)%mod

print(ans%mod)
