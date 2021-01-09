N = int(input())
S = [int(input()) for _ in range(N)]

total = sum(S)
if total%10 != 0: exit(print(total))
a = 1000
for s in S:
    if a>s and s%10 != 0:
        a = s
if a%10 == 0:
    print(0)
else:
    print(total - a)