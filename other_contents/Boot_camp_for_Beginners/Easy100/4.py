from math import floor
N = int(input())

ans = ":("
for X in range(55000):
    if floor(X*1.08) == N:
        ans = X
print(ans)