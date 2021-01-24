N = int(input())
s = input()
t = input()
ans = 2*N

for i in range(1, N+1):
    S = s + t[i:]
    if S[-N:] == t:
        ans = min(ans, len(S))

print(ans)
