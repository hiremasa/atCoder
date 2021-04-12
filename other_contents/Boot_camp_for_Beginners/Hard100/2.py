import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7
cnt = 0
for i in range(N - 1):
    A_i = A[i]
    for j in range(i + 1, N):
        if A_i > A[j]:
            cnt += 1

A.sort()
inside = 0
for i in range(N):
    inside += bisect.bisect_left(A, A[i])

print((cnt * K + inside * (K - 1) * K // 2) % MOD)