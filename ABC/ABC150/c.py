N = int(input())
from itertools import permutations

P=tuple(map(int, input().split()))
Q=tuple(map(int, input().split()))

A=list(permutations([i for i in range(1, N+1)]))
a=A.index(P)
b=A.index(Q)
print(abs(a-b))