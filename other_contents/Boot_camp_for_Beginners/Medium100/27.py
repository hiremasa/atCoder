N = int(input())
s = input()
t = input()
ans = 2*N
for i in range(len(t)):
    S = s + t[i:]
    if S[-N:] == t:
        ans = min(ans, len(S))

print(len(ans))
