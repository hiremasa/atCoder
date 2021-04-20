N = int(input())
A = list(map(int, input().split()))
mod = 998244353

if A[0] != 0:
    exit(print(0))
elif 0 in A[1:]:
    exit(print(0))
else:
    ans = 1
    prev_v = 1
    from collections import Counter
    A_c = sorted(Counter(A[1:]).items(), key=lambda x: x[0])
    for i, (k, v) in enumerate(A_c):
        #print(k, v)
        if i + 1 != k:
            exit(print(0))
        for _ in range(v):
            ans *= prev_v
            ans %= mod
            #print(ans)
        prev_v = v
    print(ans)
