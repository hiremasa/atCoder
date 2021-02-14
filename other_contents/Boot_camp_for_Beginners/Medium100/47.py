N, P = map(int, input().split())
A = list(map(int, input().split()))

A_div2 = [a%2 for a in A]

if 1 not in A_div2:
    if P == 1:
        exit(print(0))
    else:
        exit(print(2**N))
else:
    exit(print(2**(N-1)))