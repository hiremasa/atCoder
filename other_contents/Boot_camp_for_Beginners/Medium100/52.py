N = int(input())
AB = []

for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB = sorted(AB, key = lambda x: x[1])

now = 0
for a, b in AB:
    if b - now >= a:
        now += a
    else:
        exit(print("No"))
print("Yes")