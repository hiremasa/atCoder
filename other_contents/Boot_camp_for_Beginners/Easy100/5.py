from operator import mul
N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for _ in range(N):
    A = list(map(int, input().split()))
    s = list(map(mul, A, B))
    if sum(s)+C>0:
        ans += 1
        
print(ans)