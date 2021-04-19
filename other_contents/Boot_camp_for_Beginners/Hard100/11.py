from math import gcd

A, B = map(int, input().split())
g = gcd(A, B)

def prime_decomposition(n): #素因数分解
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(int(n))
    return table

print(len(set(prime_decomposition(g))) + 1)
