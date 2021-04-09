import collections
N, P = map(int, input().split())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)

    return a

c = collections.Counter(prime_factorize(P))

ans = 1
for k, v in c.items():
    if v >= N:
        ans *= k ** (v // N)
print(ans)
