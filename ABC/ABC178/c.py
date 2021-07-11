N = int(input())

if N <= 1:
    print(0)
else:
    mod = 10**9 + 7

    # for _ in range(N - 2):
    #     ans *= 10
    #     ans % mod
    # print(ans%mod)

    del1 = (9 ** N * 2) % mod - (8 ** N) % mod
    ans = (10 ** N) % mod - del1
    print(ans)
