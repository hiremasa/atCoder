N = int(input())
A = list(map(int, input().split()))
ans = len(set([a // 400 for a in A if a < 3200]))

extra = 0

for a in A:
    if a >= 3200:
        extra += 1
if extra == N:
    exit(print(1, ans + extra))

print(ans, ans + extra)
